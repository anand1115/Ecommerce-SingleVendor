from django.urls import path
from . import views

app_name="Product"

urlpatterns=[

	path("",views.ProductsView.as_view(),name="Products"),
	path("<slug>",views.ProductView.as_view(),name="Product"),

]