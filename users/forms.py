from django.forms import forms, ModelForm, Textarea
# Here is the default User model
from django.contrib.auth.models import User
# For our creation/register form we are using the default creation form
from django.contrib.auth.forms import UserCreationForm
# We are going to use pts_pops_app Profile Model to allow users to edit their profile
from pts_pops_app.models import Profile


class RegisterForm(UserCreationForm):
    # Inheriting from parent UserCreationForm
    class Meta:
        model = User
        # Since we inherit from parent we get to use their fields p1 is normal pass and p2 is confirm pass
        fields = ['username', 'password1', 'password2']


class ChangeProfilePhoto(ModelForm):
    class Meta:
        model = Profile
        fields = ['user_photo']
        labels = {
            'user_photo': 'Your Profile Picture',
        }

class ChangeProfileEmail(ModelForm):
    class Meta:
        model = Profile
        fields = ['user_email']
        labels = {
            'user_email': 'Your Email',
        }

class ChangeProfileBio(ModelForm):
    class Meta:
        model = Profile
        fields = ['user_bio']
        labels = {
            'user_bio': 'Your Biography',
        }
        # Cols just expands the length of the text box
        widgets = {'user_bio': Textarea(attrs={'cols':100})}

class ChangeUserName(ModelForm):
    password = None

    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'Your Username'
        }