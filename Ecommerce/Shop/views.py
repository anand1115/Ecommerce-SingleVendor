from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class CartView(View):

	def render(self,request,context={}):
		return render(request,"Shop/Cart.html",context)

	def get(self,request,*args,**kwargs):
		return self.render(request)


class CheckOutView(View):

	def render(self,request,context={}):
		return render(request,"Shop/CheckOut.html",context)

	def get(self,request,*args,**kwargs):
		return self.render(request)


class WishListView(View):

	def render(self,request,context={}):
		return render(request,"Shop/WishList.html",context)

	def get(self,request,*args,**kwargs):
		return self.render(request)