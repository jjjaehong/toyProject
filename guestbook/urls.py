from django.urls import path
from . import views

urlpatterns = [
    path('', views.guestbook_main, name='guestbook_main'),
    
]
