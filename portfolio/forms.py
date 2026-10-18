
from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Your full name",
                "class": "form-input",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Your email address",
                "class": "form-input",
            }),
            "subject": forms.TextInput(attrs={
                "placeholder": "Message subject",
                "class": "form-input",
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Write your message...",
                "class": "form-input",
                "rows": 5,
            }),
        }
