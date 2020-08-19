from django.urls import path
from django.http import JsonResponse
from . import views
from . import payments

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path("register/", views.register, name="register"),  # for register user

    path('payment/', payments.payment, name="payment"),  # for payment
    path('charge/', payments.charge, name="charge"),  # for payment
    path('success/<str:args>/', payments.success, name="success"),


]
