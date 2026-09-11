from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Category, Tag, ProjectPicture


def create_project(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        total_target = request.POST['total_target']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        category_id = request.POST['category']
        tag_ids = request.POST.getlist('tags')
        pictures = request.FILES.getlist('pictures')

        project = Project.objects.create(
            title=title,
            description=description,
            total_target=total_target,
            start_time=start_time,
            end_time=end_time,
            category_id=category_id
        )

        project.tags.set(tag_ids)

        for picture in pictures:
            ProjectPicture.objects.create(
                project=project,
                picture=picture
            )

        return redirect('project_details', project.id)

    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'projects/create_project.html', {
        'categories': categories,
        'tags': tags
    })


def project_details(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    similar_projects = Project.objects.filter(
        tags__in=project.tags.all()
    ).exclude(
        id=project.id
    ).distinct()

    return render(request, 'projects/project_details.html', {
        'project': project,
        'similar_projects': similar_projects
    })