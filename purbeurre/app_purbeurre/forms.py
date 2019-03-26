from django import forms

class SearchForm(forms.Form):
    research = forms.CharField(
        label="Recherche",
        widget=forms.TextInput(attrs={'placeholder': 'Trouvez un aliment', 'class': 'form-control ', 'autocomplete': 'off'})
    )

class HomeSearchForm(forms.Form):
    research = forms.CharField(
        label = 'Recherche',
        widget = forms.TextInput(attrs={'placeholder': 'Trouvez un aliment', 'class': 'form-control', 'autocomplete': 'off'})
    )