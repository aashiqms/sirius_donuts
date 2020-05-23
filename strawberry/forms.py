from django import forms
from . models import Flavour

# class StrawberryForm(forms.Form):
#     flavour = forms.ChoiceField(label='Flavour', choices=[('Strawberry', 'Strawberry'), ('Chocolate', 'Chocolate'), ('Mixed', 'Mixed'), ('Special', 'Special'), ('Jack Fruit', 'Jack Fruit'), ('Pineapple', 'Pineapple')], widget=forms.PasswordInput)
#     size = forms.ChoiceField(label='Size', choices=[('Regular', 'Regular'), ('Medium', 'Medium'), ('Large', 'Large')])


class StrawberryForm(forms.ModelForm):
    class Meta:
        model = Flavour
        fields = ['size', 'flavour']

