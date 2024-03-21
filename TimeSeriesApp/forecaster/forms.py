from django import forms
from .models import Dataset


class DatasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ['name', 'description', 'image', 'file']
        # назначеине имени для аргумента
        labels = {
            'name': 'Название Датасета',
        }
        # Стили для полей
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
