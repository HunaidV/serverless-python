from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.views.generic import ListView, FormView, TemplateView
from django.template.loader import render_to_string
# Create your views here.
from django.conf import settings
from .forms import *

from django.core.mail import EmailMessage, send_mail, get_connection, EmailMultiAlternatives


def frontmail(request ):
    if request.method != 'POST':
        form = FrontForm()
        
    
        form = FrontForm(request.POST, request.FILES)   
        if form.is_valid():
            name = form.cleaned_data['name']
            country = form.cleaned_data['country']
            Related_to = form.cleaned_data['Related_to']
            Message = form.cleaned_data['Message']
            email = form.cleaned_data['email']
            attach = request.FILES['attach']
            subject = "Form Submission on AcademiaBuddy"
            message = name + country + Related_to + email 
            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER,'academiabuddy5@gmail.com')
                mail.attach(attach.name, attach.read(), attach.content_type)
                mail.send()
                return HttpResponseRedirect('/thankyou/') 
            except:
                return HttpResponseRedirect('/order/')
        else:
            form = FrontForm
            template_name="order.html"
            return render(request, template_name, {'form': form ,}) 
        

    # if request.method == 'POST':
    #   form = FrontForm(request.POST, request.FILES)
    #   if form.is_valid():
    #     name = form.cleaned_data['name']
    #     country = form.cleaned_data['country']
    #     Related_to = form.cleaned_data['Related_to']
    #     email = form.cleaned_data['email']
    #     file = request.FILES['file']
    #     # botcheck = form.cleaned_data['botcheck'].lower()
    #     Message = form.cleaned_data['Message']
        
    #     #message1 = "name:  "+  name+ "\n" + "country :  "  + country + "\n"  + "Related_to :  " + Related_to + "\n" + "email : " + email + "\nMessage: \t"  + Message
    #     subject = "Form Submission on AcademiaBuddy"
    #     message = render_to_string('contact_template.html', {
    #         'name': name,
    #         'country': country,
    #         'Related_to': Related_to,
    #         'email': email,
    #         'message': Message,
            
    #     })    
    #     try:
    #             mail = EmailMessage(subject, message, ['alihunaid185@gmail.com'], ['alihunaid185@gmail.com'])
    #             mail.Attachment(file.name, file.read(), file.content_type)
                
    #             mail.send()
    #             return HttpResponseRedirect('/thankyou/')    
    #     except:
    #         return "Attachment error"

    #     return HttpResponseRedirect('/thankyou/')
    # else:
    #     form = FrontForm
    # template_name="order.html"
    # return render(request, template_name, {'form': form ,}) 


#my real form which is working till now##################################3
# if request.method == 'POST':
#       form = FrontForm(request.POST)
#       if form.is_valid():
#         name = form.cleaned_data['name']
#         country = form.cleaned_data['country']
#         Related_to = form.cleaned_data['Related_to']
#         email = form.cleaned_data['email']
#         # botcheck = form.cleaned_data['botcheck'].lower()
#         Message = form.cleaned_data['Message']
        
#         #message1 = "name:  "+  name+ "\n" + "country :  "  + country + "\n"  + "Related_to :  " + Related_to + "\n" + "email : " + email + "\nMessage: \t"  + Message
#         subject = "Form Submission on AcademiaBuddy"
#         message = render_to_string('contact_template.html', {
#             'name': name,
#             'country': country,
#             'Related_to': Related_to,
#             'email': email,
#             'message': Message,
            
#         })    
#         send_mail(subject, message, email, ['alihunaid185@gmail.com'])

#         return HttpResponseRedirect('/thankyou/')
#     else:
#         form = FrontForm
#     template_name="order.html"
#     return render(request, template_name, {'form': form ,}) 

#######################################################
# def contact(request):
#     if request.method == 'GET':
#         form = contact_form()
#     else:
#         form = contact_form(request.POST)
#         if form.is_valid():
#             contact_name = form.cleaned_data['contact_name']
#             contact_email = form.cleaned_data['contact_email']
#             contact_message = form.cleaned_data['contact_message']
#             try:
#                 send_mail(contact_name, contact_message, contact_email, ['californiamikegreen@yahoo.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "contact.html", {'form': form})



# def sendmail(request):
#       if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#           firstname = form.cleaned_data['firstname']
#           lastname = form.cleaned_data['lastname']
#           email = form.cleaned_data['email']
#           subject = form.cleaned_data['subject']
#           botcheck = form.cleaned_data['botcheck'].lower()
#           message = form.cleaned_data['message']
#           message1 = "firstname:  "+  firstname+ "\n" + "Lastname :  "  + lastname + "\n"  + "message :  " + message + "\n" + "email : " + email + ">"

#           if botcheck == 'yes':
#             try:
              
#               send_mail(subject, message1, email, ['alihunaid185@gmail.com'])
#               return HttpResponseRedirect('/email/thankyou/')
#             except:
#               return HttpResponseRedirect('/email/')
#         else:
#           return HttpResponseRedirect('/email/')
#       else:
#         return HttpResponseRedirect('/email/')  

 

# def home(request):
#     form = Free_Quote_Form(request.POST or None)

#     if form.is_valid():
#     	form.save(commit=False)
#     	form.save()
#     	subject = "Thankyou for your time"
#     	message = "Welcome to AcademiaBuddy"
#     	from_email = settings.EMAIL_HOST_USER
#     	to_list = ['save_it.email', settings.EMAIL_HOST_USER]
#     	send_mail(subject, message, from_email, to_list, fail_silently=False)
#     	messages.success(request, 'Thankyou')
#     	return HttpResponseRedirect('/')


# class ContactView(FormView):
#     template_name = 'contact.html'
#     form_class = ContactForm
#     success_url = '/'

#     def form_valid(self, form):
#         send_mail(
#             'ContactForm - {} - {}'.format(form.cleaned_data.get('contact_email'),
#                                        form.cleaned_data.get('contact_name')),
#             form.cleaned_data.get('content'),
#             settings.EMAIL_FROM,
#             settings.EMAIL_TO,
#             fail_silently=False,
#         )
#         return super(ContactView, self).form_valid(form)
