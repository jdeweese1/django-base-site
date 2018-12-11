from django import forms
from django.utils import timezone

from .models import Contact


class ContactCreateForm(forms.ModelForm):
    sender_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailInput()
    subject = forms.CharField(max_length=50, required=True)
    message = forms.CharField(max_length=200, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sender_name'].required = True
        self.fields['email'].required = True
        self.fields['subject'].required = True
        self.fields['message'].required = True

    class Meta:
        model = Contact
        exclude = ('created',)

    def save(self, commit=True):
        self.instance.created = timezone.now()
        self.instance.save()
