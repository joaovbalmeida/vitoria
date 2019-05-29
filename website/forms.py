from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(
        attrs={'class': 'half-form', 'placeholder': 'Nome'}
    ))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}
    ))
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(
        attrs={'placeholder': 'Mensagem', 'rows': 5, 'cols': 30}
    ))