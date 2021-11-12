from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<em>This is responce of pro two</em>")

def help(request):
    dict={'name':"ashwini"}
    return render(request, 'appTwo/help.html',context=dict)
