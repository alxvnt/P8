from django import forms


class CommentaryForm(forms.Form):
    commentary = forms.CharField(
        label = "",
        widget=forms.TextInput(attrs={'placeholder': 'Votre avis', 'class': 'form-control ', 'autocomplete': 'off'})
    )
