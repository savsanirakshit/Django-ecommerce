from . import views
from django.urls import path

app_name = "app"

urlpatterns = [
    path('cart', views.cart, name="cart"),
    path('order_summary', views.OrderSummaryView.as_view(), name="order_summary"),
    path('', views.HomeView.as_view(), name="home"),
    path('home', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('details/<slug>/', views.ItemDetailView.as_view(), name="details"),
    path('add_to_cart/<slug>/', views.add_to_cart, name="add_to_cart"),
    path('remove_from_cart/<slug>/', views.remove_from_cart, name="remove_from_cart"),
    path('remove_item_from_cart/<slug>/', views.remove_single_item_from_cart, name="remove_single_item_from_cart"),
]