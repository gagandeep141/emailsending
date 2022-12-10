from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name=forms.CharField(max_length=120)
    email=forms.EmailField()
    inquiry=forms.CharField(max_length=80)
    message=forms.CharField(widget=forms.Textarea)

    def get_info(self):
        # cleaned data
        cl_data=super().clean()

        name=cl_data.get('name').strip()
