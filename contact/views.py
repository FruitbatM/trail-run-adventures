from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from .forms import ContactForm
from profiles.models import UserProfile


def contact(request):
    """
    A view to return the contact page and render the form.
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            full_name = contact_form.cleaned_data['full_name']
            user_email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(
                    # to capture the user email it's displayd in the
                    # subject field
                    f"Message from {full_name}, <{user_email}>",
                    message,
                    user_email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False
                )
                return redirect('contact_thankyou')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            if request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user)
                user_email = profile.user.email
                contact_form = ContactForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.default_email,
                    })
            else:
                contact_form = ContactForm()

        context = {
            'contact_form': contact_form,
        }

        return render(request, 'contact/contact.html', context)
