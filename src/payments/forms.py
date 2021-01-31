from django import forms
from .models import Account, BookUpload, BookDisplay

class AccountForm(forms.ModelForm):
    name = forms.TextInput()
    class Meta:
        model = Account
        fields = [
            'name',
        ]
        labels = {
            'name': 'Name',
        }

class CustomerForm(forms.ModelForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    street_number = forms.TextInput()
    street_name = forms.TextInput()
    city = forms.TextInput()
    state = forms.TextInput()
    zip = forms.TextInput()

class BookForm(forms.ModelForm):
    class Meta:
        model = BookUpload
        fields = [
            'user_id',
            'title',
            'author',
            'price',
            'shipping',
           'picture'
        ]

class BookDisplay(forms.ModelForm):
    class Meta:
        model = BookDisplay
        fields = [
            'name'
        ]