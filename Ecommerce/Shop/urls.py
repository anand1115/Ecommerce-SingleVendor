from django.urls import path
from . import views
app_name="Shop"

urlpatterns=[
	path('',views.CartView.as_view(),name="Cart"),
	path('checkout/',views.CheckOutView.as_view(),name="CheckOut"),
	path('wishlist/',views.WishListView.as_view(),name="WishList"),
	path("updatecart/",views.UpdateCart.as_view(),name="UpdateCart"),
]
	