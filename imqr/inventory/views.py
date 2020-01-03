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
        return redirect('/login')
    else:   
        return render(request,template_name='imqr/index.html')

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