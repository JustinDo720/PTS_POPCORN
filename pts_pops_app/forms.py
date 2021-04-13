from .models import Post
from django import forms

class UserEntries(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['comments', 'picture']
        labels = {'comments': 'What would you like to share?', 'picture': 'Upload photos of your popcorn!'}
        widgets = {'comments': forms.Textarea(attrs={'cols': 100})}


class EditUserEntries(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['comments', 'picture']
        labels = {'comments': 'What would you like to change?', 'picture': 'Upload a replacement photo of your popcorn!'}
        widgets = {'comments': forms.Textarea(attrs={'cols':100})}