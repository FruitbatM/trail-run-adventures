from django.shortcuts import render
from .models import Instructor


def our_story(request):
    """
    A view to return Trail Run Adventures story page.
    """
    return render(request, 'about/our_story.html')


def our_team(request):
    """
    A view to show the team information. Team data (name, title and about)
    will be returning from the Team model.
    """
    instructors = Instructor.objects.all()
    context = {
        'instructors': instructors,
    }
    return render(request, 'about/our_team.html', context)


def contact(request):
    """
    A view to return the contact page and render the form.
    """
    return render(request, 'about/contact.html')
