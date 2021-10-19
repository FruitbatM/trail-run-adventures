from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from .forms import ContactForm
from profiles.models import UserProfile


def contact(request):
    """ View to render contact page with contact form """

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            user_email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(
                    # to capture the user email
                    f"Message from {name}, <{user_email}>",
                    message,
                    user_email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False
                )
                return redirect('contact_success')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    else:
        # Attempt to prefill the users's full_name and email, if they have
        # this information saved in the profile
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            user_email = profile.user.email
            contact_form = ContactForm(initial={
                'email': user_email,
                })
        else:
            contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request):
    """
    A view to return contact_success page in order \
        to inform user that the message was successfully sent
    """
    return render(request, 'contact/contact_success.html')
