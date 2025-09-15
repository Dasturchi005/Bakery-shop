from django.urls import path
from .views import product_list , product_info
urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', product_info, name='info'),
]
