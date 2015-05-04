from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('username', 'email', 'password')
=======
        fields = ('username', 'email', 'password')
>>>>>>> 12ac29542bead9f3a893f6d87f212c8d6f278e5d
