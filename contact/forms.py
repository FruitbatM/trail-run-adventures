from django import forms


class ContactForm(forms.Form):
    """
    Contact form for Contact Page
    """
    full_name = forms.CharField(required=True, label="Full Name")
    email = forms.EmailField(required=True, label="Email")
    subject = forms.CharField(required=False, label="Subject")
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        fields = ['full_name', 'email', 'subject' 'message']
