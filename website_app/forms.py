from django import forms
import re


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, required=True,  label='Imię:', error_messages={
        'required': "Imię nie może być puste!",
    })
    subject = forms.CharField(max_length=60, required=True, error_messages={
        'required': "Temat nie może być pusty!"
    })
    email = forms.EmailField(required=True, error_messages={
        'required': "Email nie może być pusty!",
        'invalid': "Podaj poprawny adres e-mail!"
    })
    message = forms.CharField(widget=forms.Textarea, required=True, error_messages={
        'required': "Wiadomość nie może być pusta!"
    })

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if len(name) < 2:
            raise forms.ValidationError("Imię musi mieć conajmniej 2 znaki!")

        for letter in name.replace(" ", ""):
            if not letter.isalpha():
                raise forms.ValidationError("Imię nie może zawierać cyfr!")

        return name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(email_regex_pattern, email):
            raise forms.ValidationError("Podaj poprawny adres email!")

        return email

    def clean_subject(self):
        subject = self.cleaned_data.get("subject")

        if len(subject) < 3:
            raise forms.ValidationError("Temat musi mieć conajmniej 3 znaki!")

        return subject

    def clean_message(self):
        message = self.cleaned_data.get("message")

        if len(message) < 10:
            raise forms.ValidationError("Wiadomość musi miec conajmniej 10 znaków!")

        return message
