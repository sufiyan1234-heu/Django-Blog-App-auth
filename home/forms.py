from django import forms
from .models import Contact3


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact3
        fields = ['company', 'email', 'phone', 'desc']
