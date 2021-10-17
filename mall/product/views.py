from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm

# Create your views here.
class ProductList(ListView):
    model = Product 
    template_name = 'product.html'

class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm 
    success_url = '/product/'
    
class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    # 아래 내용을 설정하면 for item in product 처럼
    # 사용할 수 있음 -> humanize
    context_object_name = 'product'