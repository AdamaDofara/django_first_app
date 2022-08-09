from django import forms
from django.forms import ModelForm, ValidationError

from produit.models import Produit


class ProduitForm(forms.ModelForm):
    nom = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'nom du produit'}))
    prix = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'prix'}))
    photo = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    description = forms.Textarea(attrs={'class':'form-control'})
    class Meta:
        model = Produit
        fields = { 'nom','prix','photo','description'}


    def clean_nom(self):
        nomm = self.cleaned_data['nom']
        try:
            _nom = Produit.objects.get(nom=nomm)
            _nom = _nom.nom
        except Produit.DoesNotExist:
            _nom = None

        if _nom is not None:
            raise ValidationError("Ce nom de produit existe déja ! "+_nom)
        else:
            return nomm