import email
from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import models
from django.contrib import messages

# Create your views here.
def index(request):
    context = None
    template = 'main_project/index.html'
    return render(request, template, context)

def get_started(request):
    context = None
    template = 'main_project/get-started.html'
    return render(request, template, context)

def contact(request):
    context = None
    template = 'main_project/contact.html'
    return render(request, template, context)

def pricing(request):
    context = None
    template = 'main_project/pricing.html'
    return render(request, template, context)

def confirmation_project(request, type):

    context = {
        'type':type
    }

    template = 'main_project/confirmation.html'
    return render(request, template, context)

def project_reqeust(request):
    if request.method == 'POST':

        post = request.POST
        print('post : ', post)
        project_type = request.POST['project_type']
        email = request.POST['email']
        message = request.POST['message']

        print(project_type,email,message)
        print(all([project_type, email, message]))

        if all([project_type, email, message]):
            models.ProjectRequest(
                project_type = project_type,
                email = email,
                message = message
            ).save()

            return JsonResponse({'status' : 200})
        return JsonResponse({'status' : 400})

def contect_us(request):
    
    if request.method == 'POST':
        name = request.POST['first_name']
        email = request.POST['email']
        number = request.POST['mobile']
        message = request.POST['message']

        if all([name, email, number, message]):
            models.Contact(
                client_name = name,
                client_email = email,
                client_mobile = number,
                client_message = message,
            ).save()
        
            return redirect('thank-you', name=name)
            
        messages.info(request, 'All fields are required !')
        return redirect('contact')

def thank_you(request, name):
    name_globle = name
    return render(request, 'main_project/thank-you.html', {'name' : name_globle})

        