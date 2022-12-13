from django.urls import path
from . import views

urlpatterns = [
    #sets url path to home page
    path('', views.home, name='index'),
    #sets url path to Create New Account page
    path('create/', views.create_account, name='create'),
    #sets url path to the Balance Sheet page
    path('<int:pk>/balance/', views.balance, name='balance'),
    #sets url path to Add New Transaction page
    path('transaction/', views.transaction, name='transaction'),
]
