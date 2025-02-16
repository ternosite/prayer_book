from django import forms
from .models import Psalm


class PsalmForm(forms.ModelForm):
    class Meta:
        model = Psalm
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 
                                           'placeholder': 'Назва псалму'}), 
            'text': forms.Textarea(attrs={'class': 'form-control', 
                                           'placeholder': 'Текст псалму'})
        }
        labels = {
            'name': 'Назва', 
            'text': 'Текст', 
        }
        error_messages = {
            'name': {
                'required': 'Поле "Назва псалму" є обов’язковим'
            }
        }