from django.shortcuts import render
from .models import Contact 
from django.http import HttpResponse
from django.core.mail import send_mail 

# Create your views here.
def index(request): 
    if request.method == "POST":
        
        contact = Contact() 
        name = request.POST.get('name')
        email = request.POST.get('email')
        subjectline = request.POST.get('subjectline')
      
        data = {
            'name': name, 
            'email': email, 
            'subject': name, 
            'message': subjectline
        }
        #send email from gmail smtp server 
        send_mail( 
            data['name'], 
            data['message'],
            ['digitallynked@gmail.com'], 
        )
        contact.name=name 
        contact.email=email 
        contact.subjectline=subjectline
        contact.save()
        return(request, 'myconsultant/index.html', {})

    return render(request, 'myconsultant/index.html', {})
