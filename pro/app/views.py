from http.client import HTTPResponse

from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

#function based

# def Home(request):
#     if(request.method=='GET'):
#
#         return HttpResponse('welcome to django')


#define index view returns message 'index page'

# def Index(request):
#     if(request.method=='GET'):
#         return HttpResponse('index page')

#class based

from django.views import View

class Home(View):
    def get(self,request):
        return HttpResponse('welcome to django')

class Index(View):
    def get(self,request):
        return HttpResponse('Index')