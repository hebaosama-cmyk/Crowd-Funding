from django.shortcuts import render, get_object_or_404, redirect
from .models import Donation
from projects.models import Project

def donation_page(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        amount = request.POST.get('amount')

        if amount and float(amount) > 0:
            Donation.objects.create(
                user=request.user,
                project=project,
                amount=amount
            )

            return redirect('project_details', project.id)

        else:
            return render(request, 'donations/donation.html', {
                'project': project,
                'error': 'Donation amount must be greater than 0.'
            })

    return render(request, 'donations/donation.html', {
        'project': project
    })