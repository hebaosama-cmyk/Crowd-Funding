from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'mobile_number',
            'profile_picture',
            'birthdate',
            'facebook_profile',
            'country',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            'mobile_number': forms.TextInput(attrs={
                'placeholder': 'Egyptian Mobile Number'
            }),
            'birthdate': forms.DateInput(attrs={
                'type': 'date'
            }),
            'facebook_profile': forms.URLInput(attrs={
                'placeholder': 'Facebook Profile URL'
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'Country'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'An account with this email already exists.'
            )

        return email

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')

        if not mobile_number:
            raise forms.ValidationError(
                'Mobile number is required.'
            )

        if not mobile_number.isdigit():
            raise forms.ValidationError(
                'Enter a valid Egyptian mobile number.'
            )

        if len(mobile_number) != 11:
            raise forms.ValidationError(
                'Egyptian mobile number must contain 11 digits.'
            )

        if not mobile_number.startswith(('010', '011', '012', '015')):
            raise forms.ValidationError(
                'Enter a valid Egyptian mobile number.'
            )

        return mobile_number

    def save(self, commit=True):
        user = super().save(commit=False)

        user.username = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password'
        })
    )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'mobile_number',
            'profile_picture',
            'birthdate',
            'facebook_profile',
            'country',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name'
            }),
            'mobile_number': forms.TextInput(attrs={
                'placeholder': 'Egyptian Mobile Number'
            }),
            'birthdate': forms.DateInput(attrs={
                'type': 'date'
            }),
            'facebook_profile': forms.URLInput(attrs={
                'placeholder': 'Facebook Profile URL'
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'Country'
            }),
        }

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')

        if not mobile_number:
            raise forms.ValidationError(
                'Mobile number is required.'
            )

        if not mobile_number.isdigit():
            raise forms.ValidationError(
                'Enter a valid Egyptian mobile number.'
            )

        if len(mobile_number) != 11:
            raise forms.ValidationError(
                'Egyptian mobile number must contain 11 digits.'
            )

        if not mobile_number.startswith(('010', '011', '012', '015')):
            raise forms.ValidationError(
                'Enter a valid Egyptian mobile number.'
            )

        return mobile_number