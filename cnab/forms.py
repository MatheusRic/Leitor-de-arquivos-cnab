from django import forms

class form(forms.Form):
    file = forms.FileField(label="Buscar Arquivo")