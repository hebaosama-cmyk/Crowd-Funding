from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import EditProfileForm, LoginForm, RegistrationForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            activation_link = request.build_absolute_uri(
                reverse(
                    'activate',
                    kwargs={
                        'uidb64': uid,
                        'token': token,
                    }
                )
            )

            send_mail(
                subject='Activate your Crowd-Funding account',
                message=(
                    f'Hello {user.first_name},\n\n'
                    f'Please click the link below to activate your account:\n\n'
                    f'{activation_link}\n\n'
                    f'This activation link will expire after 24 hours.'
                ),
                from_email=None,
                recipient_list=[user.email],
            )

            messages.success(
                request,
                'Registration successful. Please check your email to activate your account.'
            )

            return redirect('register')

    else:
        form = RegistrationForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):

        if timezone.now() - user.date_joined <= timedelta(hours=24):
            user.is_active = True
            user.save(update_fields=['is_active'])

            messages.success(
                request,
                'Your account has been activated successfully. You can now log in.'
            )

            return redirect('login')

    messages.error(
        request,
        'The activation link is invalid or has expired.'
    )

    return redirect('register')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=email,
                password=password
            )

            if user is not None:
                login(request, user)

                messages.success(
                    request,
                    'Login successful.'
                )

                return redirect('profile')

            messages.error(
                request,
                'Invalid email or password, or your account is not activated.'
            )

    else:
        form = LoginForm()

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


def logout_view(request):
    logout(request)

    messages.success(
        request,
        'You have been logged out successfully.'
    )

    return redirect('login')


@login_required
def profile(request):
    return render(
        request,
        'accounts/profile.html'
    )


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Your profile has been updated successfully.'
            )

            return redirect('profile')

    else:
        form = EditProfileForm(
            instance=request.user
        )

    return render(
        request,
        'accounts/edit_profile.html',
        {'form': form}
    )


@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user

        logout(request)
        user.delete()

        messages.success(
            request,
            'Your account has been deleted successfully.'
        )

        return redirect('register')

    return render(
        request,
        'accounts/delete_account.html'
    )