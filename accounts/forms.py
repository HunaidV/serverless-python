from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=30, required=True, help_text='Only your first name')
    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['username'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['email'].help_text = ''
    	

    class Meta:
        model = User
        fields = ('username', 'full_name',  'email', 'password1', 'password2', )