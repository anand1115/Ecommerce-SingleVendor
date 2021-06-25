from django.urls import path
from . import views 
app_name="Home"

urlpatterns=[
	path('',views.HomeView.as_view(),name="Home"),
	path('profile/',views.ProfileView.as_view(),name="Profile"),
	path('contact/',views.ContactView.as_view(),name="Contact"),
]