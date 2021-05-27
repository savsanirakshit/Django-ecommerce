from . import views
from django.urls import path

app_name = "app2"

urlpatterns = [
    path('cart', views.cart, name="cart"),
    path('payment/<payment_options>/', views.PaymentView.as_view(), name='payment'),
    path('', views.Checkout.as_view(), name="checkout"),
    path('home', views.home, name="home"),
    path('logout', views.logout, name="logout"),
]