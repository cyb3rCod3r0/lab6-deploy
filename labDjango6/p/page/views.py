from pdb import post_mortem
from django.shortcuts import render
from django.http import HttpResponse
from . models import Page

# Create your views here.
#for home page aka index
def home(request):
    return render(request, 'page/home.html')

#for about page
def about(request):
    return render(request, 'page/about.html')

#for contact page
def contact(request):
    if request.method == "POST":
        page = Page()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        page.name = name
        page.email = email
        page.subject = subject
        page.message = message
        page.save()

    return render(request, 'page/contact.html',{'post':post_mortem})

#for frequent asked question
def faq(request):
    return render(request, 'page/fAQ.html')

