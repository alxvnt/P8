from django import forms


class LoginForm(forms.Form):
    pseudo = forms.CharField(
        label="Pseudo",
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Votre pseudo', 'class': 'form-control'}),
        required=True
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs=
                                   {'placeholder': 'Mot de passe', 'class': 'form-control', 'autocomplete': 'off'}),
        required=True
    )



class RegisterForm(forms.Form):
    pseudo = forms.CharField(
        label="Pseudo",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required = True

    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Mot de passe', 'class': 'form-control', 'autocomplete': 'off'}),
        required = True
    )

class SearchForm(forms.Form):
    research = forms.CharField(
        label = "Recherche",
        widget = forms.TextInput(attrs={'placeholder': 'Trouvez un aliment', 'class': 'form-control'})
    )