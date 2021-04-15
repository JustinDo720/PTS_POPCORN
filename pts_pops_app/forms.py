from .models import Post, Feedback
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


class AnonymousEntries(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['comments', 'picture']
        labels = {'comments': 'Please share your thoughts!', 'picture': 'Upload photos of your popcorn!'}
        widgets = {'comments': forms.Textarea(attrs={'rows':3})}


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['opinions', 'good', 'name']
        labels = {'opinions': 'What should I do differently? Any general things that I should improve on? (besides designing)',
                  'good': "What do you think?",
                  'name': "You do not have to share your name if you don't want to"
                  }