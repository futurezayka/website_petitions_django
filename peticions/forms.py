from .models import Peticions
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class PeticionsForm(ModelForm):

    class Meta:
        model = Peticions
        fields = ['title', 'text', "name_surname"]
        widgets = {
            "name_surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'

            }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title of petition'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of your petition'
            })

        }
