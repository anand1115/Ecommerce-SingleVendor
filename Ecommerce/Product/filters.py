import django_filters
from .models import Product
class ProductListFilter(django_filters.FilterSet):
	 class Meta:
	 	model=Product
	 	fields=['selling_price','discount']