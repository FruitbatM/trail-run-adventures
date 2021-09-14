from django import forms


class ContactForm(forms.Form):
    """
    Contact form for Contact Us Page
    """

    full_name = forms.CharField(required=True, label="Full Name")
    email = forms.EmailField(required=True, label="Email")
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        fields = ['full_name', 'email', 'message']
