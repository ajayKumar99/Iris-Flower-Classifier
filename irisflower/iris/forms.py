from django import forms

class IrisForm(forms.Form):
    sep_length = forms.DecimalField()
    sep_width = forms.DecimalField()
    pet_length = forms.DecimalField()
    pet_width = forms.DecimalField()

