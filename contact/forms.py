from django import forms


class ContactForm(forms.Form):
    """
    Contact form for Contact Page
    """
    name = forms.CharField(required=True, label="Name")
    email = forms.EmailField(required=True, label="Email")
    subject = forms.CharField(required=False, label="Subject")
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        fields = ['name', 'email', 'subject' 'message']
