from django import forms

class SearchForm(forms.Form):
    pokemon_type = forms.CharField(max_length=100, label="Pokemon Type")