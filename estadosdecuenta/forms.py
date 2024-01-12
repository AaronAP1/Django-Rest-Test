# En forms.py
from django import forms

class ExcelImportForm(forms.Form):
    file = forms.FileField()
