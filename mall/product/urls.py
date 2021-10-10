from django.urls import path
from product.views import ProductList
from product.views import ProductCreate

urlpatterns = [
    path('', ProductList.as_view()),
    path('create/', ProductCreate.as_view()),
]