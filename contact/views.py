from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from .forms import ContactForm
from profiles.models import UserProfile


def contact(request):
    """ View to render contact page with contact form """

    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                    'name': profile.default_full_name,
                    'from_email': profile.default_email_address,
                    }
                )
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            full_name = contact_form.cleaned_data['full_name']
            message = contact_form.cleaned_data['message']
            subject = contact_form.cleaned_data['subject']
            try:
                send_mail(
                    f"Message from {full_name}",
                    subject,
                    message,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False
                    )

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/contact',
                            messages.success(request, 'Dear '
                                             + full_name.title() + ', thank you for reaching out! \
                                    We will get in touch shortly.'))

    return render(request, "contact/contact.html",
                  {'contact_form': contact_form})
