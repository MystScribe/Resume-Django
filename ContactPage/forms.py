from django import forms
from .models import ContactUsReceiveForm


class ContactUsReceiveFormForm(forms.ModelForm):
    class Meta:
        model = ContactUsReceiveForm
        fields = '__all__'