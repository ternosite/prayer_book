from django import forms
from .models import Prayer

class PrayerForm(forms.ModelForm):
    class Meta:
        model = Prayer
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва молитви'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст молитви'}),
        }
        labels = {
            'name': 'Назва', 
            'text': 'Текст', 
        }