from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('mail', views.mail, name='mail')
]