from django.urls import path
from product.views import ProductList
from product.views import ProductCreate
from product.views import ProductDetail

urlpatterns = [
    path('', ProductList.as_view()),
    path('create/', ProductCreate.as_view()),
    # primary key
    path('<int:pk>/', ProductDetail.as_view())
]