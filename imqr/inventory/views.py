from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
'''
Home Page
'''
def index(request):
    #check user is authenticated or redirect him to login page
    if not request.user.is_authenticated:
        return render(request,template_name='inventory/index.html')
    else:   
        return render(request,template_name='inventory/index.html')

'''
List all Product
'''
def productindex(request):
    return HttpResponse('nej')

'''
List specific product
'''
def productview(request,pk):
    return HttpResponse(str(pk))

'''
view for specific product
'''
def productcreate():
    pass

'''
Login Function
'''
def login(req):
    pass

'''
Register Function
'''
def register(request):
    return render(request,template_name='inventory/register/register.html')