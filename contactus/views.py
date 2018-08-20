from django.shortcuts import render
from django.core.mail import EmailMessage
# Create your views here.
from django.urls import reverse
from .forms import Contactform
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def contactmail(request):
    if request.method == 'POST':
      form = Contactform(request.POST)
      if form.is_valid():
        name = form.cleaned_data['name']
        
        email = form.cleaned_data['email']
        # botcheck = form.cleaned_data['botcheck'].lower()
        feedback = form.cleaned_data['feedback']
        
        #message1 = "name:  "+  name+ "\n" + "country :  "  + country + "\n"  + "Related_to :  " + Related_to + "\n" + "email : " + email + "\nMessage: \t"  + Message
        subject = "Form Submission on AcademiaBuddy"
        message = render_to_string('c_template.html', {
            'name': name,
            
            'email': email,
            'feedback': feedback,
            
        })    
        send_mail(subject, message, email, ['academiabuddy@gmail.com'])

        return HttpResponseRedirect(reverse('contact:thankyou'))
    else:
        form = Contactform
    template_name="contact.html"
    return render(request, template_name, {'form': form ,})       
