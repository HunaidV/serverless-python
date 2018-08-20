from django import forms
from .models import OrderModel


class OrderForm(forms.ModelForm):
	class Meta:
		model = OrderModel
		fields = [
			'name',
			
			'email',
			'Phone_Number',		
			'country', 	
			'Related_to',
			'file',
			
			'Academic_Level',	
			'Type_of_Paper', 
			'Subject',
			'Number_of_Pages',
			'Sources',
			'spacing',
			'title',
			'Paper_Details',
			'Order_Deadline',
			

	
				
				]

				 