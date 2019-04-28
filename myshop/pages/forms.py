from django import forms
from .models import Snippet





class SnippetForm(forms.ModelForm):
    
    class Meta:
        model = Snippet
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control form-control-lg form__input',
            'placeholder': 'Your Full Name', 'type': 'text', 'style': 'font-size:2rem',
            'style': 'padding:2.5rem'}),
            'email': forms.EmailInput(attrs={'class':'form-control form-control-lg form__input',
            'placeholder': 'Your Email', 'type': 'email', 'style': 'font-size:2rem',
            'style': 'padding:2.5rem'}),
            'message': forms.Textarea(attrs={'class':'form-control form-control-lg',
            'placeholder': 'Write Your Message Here...'}),
        }