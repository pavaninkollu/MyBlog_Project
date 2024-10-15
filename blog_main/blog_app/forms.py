from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a comment'}),
        }
