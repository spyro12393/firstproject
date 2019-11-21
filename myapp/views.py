from django.shortcuts import render
from datetime import datetime

# Create your views here.
def sayhello(request, username):
    now = datetime.now()
    return render(request, "hello3.html", locals())

def hello4(request, username):
    now = datetime.now()
    return render(request, "hello4.html", locals())

def jquerytest(request):
    return render(request, 'jquerytest.html', locals())

def bootstraptest(request):
    return render(request, 'bootstraptest.html', {})

def welcome(request):
    return render(request, "welcome.html", locals())