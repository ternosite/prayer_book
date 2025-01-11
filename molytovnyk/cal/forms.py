from django import forms
from .models import Holiday


class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = ['name', 'description', 'date']
        widgets = {
          'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва свята'}),
          'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Назва свята'}),  
          'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
        labels = {
            'name': 'Назва свята',
            'description': 'Опис',
            'date': 'Дата святкування'
        }