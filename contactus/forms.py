from django import forms


class Contactform(forms.Form):
	name = forms.CharField(max_length="50")
	email	= forms.EmailField(max_length="254", help_text="Enter your email")
	feedback 	= forms.CharField(max_length="1000")


	