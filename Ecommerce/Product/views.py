from django.shortcuts import render,redirect
from django.views.generic import View
from django.core.paginator import Paginator
from .filters import ProductListFilter
from .models import *

# Create your views here

class ProductView(View):

	def render(self,request,context={}):
		return render(request,"Product/Product.html",context)

	def get(self,request,slug,*args,**kwargs):
		context={}
		try:
			product=Product.objects.get(slug=slug)
		except Exception as err:
			return redirect('Home:Home')
		context['product']=product
		return self.render(request,context)


class ProductsView(View):

	def render(self,request,context={}):
		return render(request,"Product/Products.html",context)

	def get(self,request,*args,**kwargs):
		context={}
		context['products']=self.get_products(request)
		paginator=Paginator(context['products'],5)
		try:
			page_number=int(request.GET.get('page',1))
		except:
			page_number=1	
		context['page_range']=self.get_page_list(paginator,page_number)
		context['paginator']=paginator.get_page(page_number)
		return self.render(request,context)

	def get_products(self,request):
		if(request.GET.get('search',None)):
			search=request.GET.get('search')
			products=Product.objects.filter(title__icontains=search)
		else:
			products=Product.objects.all()
		data=ProductListFilter(request.GET,queryset=products)
		return data.qs.distinct()

	@staticmethod
	def get_page_list(paginator,page_number):
		page_list=paginator.page_range
		if(page_number in page_list and len(page_list)>5 and page_number>4):
			index=page_list.index(page_number)
			page_list=page_list[index-4:index+1]
		else:
			page_list=page_list[:5]
		return page_list





