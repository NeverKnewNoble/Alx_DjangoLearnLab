from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

<<<<<<< HEAD
=======
    # LibraryProject/bookshelf/forms.py

from django import forms
>>>>>>> 575d54c4aa0fd29d7edaff798bcbc16292a9012c

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must be from the domain @example.com")
        return email
