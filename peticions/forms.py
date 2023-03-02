from .models import Peticions
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class PeticionsForm(ModelForm):
    class Meta:
        model = Peticions
        fields = ['title', 'text', 'date']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title of petition'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of your petition'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of creating'

            })

        }
