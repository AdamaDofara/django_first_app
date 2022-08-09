import django_filters
from django import forms
from django.core.exceptions import ValidationError

from client.models import Client


class FormulaireCLient(forms.ModelForm):
    nom = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre nom'}))
    telephone = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre numero à 10 chiffres'}))

    class Meta:
       model = Client
       fields = {'telephone','nom'}
     #  widgets = {
          # 'nom':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre nom'}),
           #'telephone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre numero à 10 chiffres'})
       #}#

    def clean_nom(self):
       nom = self.cleaned_data['nom']
       if "a" not in nom:
           raise ValidationError("Le nom doit contenir un A!")
       return nom
    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        if len(telephone) < 8:
            raise ValidationError("Le numero de telephone doit etre de 10 chiffres")
        return telephone


