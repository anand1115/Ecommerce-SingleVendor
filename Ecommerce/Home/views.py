from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from Shop.cart import Cart

# Create your views here.

class HomeView(View):

	def render(self,request,context={}):
		return render(request,"Home/Home.html",context)

	def get(self,request,*args,**kwargs):
		context={}
		context['cart']=Cart(request)
		return self.render(request,context)

class ContactView(View):

	def render(self,request,context={}):
		return render(request,"Home/Contact.html",context)

	def get(self,request,*args,**kwargs):
		context={}
		context['cart']=Cart(request)
		return self.render(request,context)

class ProfileView(View):

	def render(self,request,context={}):
		return render(request,"Home/Profile.html",context)

	def get(self,request,*args,**kwargs):
		context={}
		context['cart']=Cart(request)
		return self.render(request,context)

