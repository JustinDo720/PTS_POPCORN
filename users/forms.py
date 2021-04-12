from django.forms import forms
# Here is the default User model
from django.contrib.auth.models import User
# For our creation/register form we are using the default creation form
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    # Inheriting from parent UserCreationForm
    class Meta:
        model = User
        # Since we inherit from parent we get to use their fields p1 is normal pass and p2 is confirm pass
        fields = ['username', 'password1', 'password2']



