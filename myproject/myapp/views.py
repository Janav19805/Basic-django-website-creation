from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')

def websitepage(request):
    return render(request,'website.html')

def formpageview(request):
    return render(request, 'form.html')


def formpageprocess(request):
    a = int(request.POST["txt1"])
    b = int(request.POST["txt2"])
    c = a + b
    return render(request,"ans.html",{'mya' :a, 'myb' :b, 'sum' :c})

