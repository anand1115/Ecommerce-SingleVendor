from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .cart import Cart
from Product.models import *
from Accounts.models import User


# Create your views here.

class CartView(View):

	def render(self,request,context={}):
		return render(request,"Shop/Cart.html",context)

	def get(self,request,*args,**kwargs):
		context={}
		context['cart']=Cart(request)
		return self.render(request,context)


class CheckOutView(View):

	def render(self,request,context={}):
		return render(request,"Shop/CheckOut.html",context)

	def get(self,request,*args,**kwargs):
		context={}
		context['cart']=Cart(request)
		return self.render(request,context)


class WishListView(View):

	def render(self,request,context={}):
		return render(request,"Shop/WishList.html",context)

	def get(self,request,*args,**kwargs):
		context={}
		context['cart']=Cart(request)
		return self.render(request,context)


class UpdateCart(View):

	# @method_decorator(login_required())
	def get(self,request):
		error=False
		if not request.user.is_authenticated:
			return redirect("Accounts:login")
		try:
			cart=Cart(request)
			if(request.is_ajax()):
				action=request.GET.get('action',None)
				productid=request.GET.get('productid',None)
				if(action and productid):
					try:
						product=Product.objects.get(id=productid)
					except Exception as err:
						print(err)
						return JsonResponse({"status":False,"message":"Product Not Found"},safe=False,status=400)
					if(action=="increment"):
						cart.add(product)
					elif(action=="decrement"):
						cart.remove(product)
					elif(action=="remove"):
						cart.clear(product)
					return JsonResponse({"status":True,"message":"Updated Successfully","cart_count":cart.count()},safe=False,status=200)
				else:
					return JsonResponse({"status":False,"message":"Please try Again later."},safe=False,status=400)
			else:
				return JsonResponse({"status":True,"message":"Updated Successfully","cart_count":cart.count()},safe=False,status=200)
		except Exception as err:
			print(err)
			return JsonResponse({"status":False,"message":"{}".format(err)},safe=False,status=400)











