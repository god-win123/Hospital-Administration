from django.urls import path
from .import views

urlpatterns = [
    path('', views.Hospital,name='Hospital'),
    path('About/',views.About,name='About'),
    path('Department/',views.Department,name='Department'),
    path('Contact/',views.Contact,name='Contact'),
    path('doctors/',views.doctors,name='doctors'),
    path('booking/',views.booking,name='booking')
]