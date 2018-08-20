from django import forms
from .models import CareerModel


class CareerForm(forms.ModelForm):
	class Meta:
		model = CareerModel
		fields = [
			'name',
			
			'email',
			'Phone_Number',		
			'country', 	
			'Applying_For',
			'file',
			'skype_id',
			'Linkedin_profile',
			'Describe_yourself',
			
			]
				 