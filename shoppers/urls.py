from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/',views.auth, name="auth"),
    path('services/', views.services, name ="services"),
    path("product-list/", views.product_list, name="product_list"),
    path("product-detail/<int:pk>/", views.product_detail, name='product_detail')
]
