from django import forms

class DataFrameForm(forms.Form):
    csv_file = forms.FileField(label='Выберите CSV файл')