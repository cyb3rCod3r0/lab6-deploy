from django.shortcuts import render

# Create your views here.
def shalle1(request):
    return render(request,'shalles/shalle1.html')

def shalle2(request):
    return render(request,'shalles/shalle2.html')

def shalle3(request):
    return render(request,'shalles/shalle3.html')

def shalle4(request):
    return render(request,'shalles/shalle4.html')