from django import forms
from .models import Product

class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': '상품명을 입력해주세요.'
        },
        max_length=64, label='상품명'
    )
    price = forms.IntegerField(
        error_messages={
            'required': '상품가격을 입력해주세요.'
        }, label='상품가격'
    )
    description = forms.CharField(
        error_messages={
            'required': '상품설명을 입력해주세요.'
        }, label='상품설명'
    )
    stock = forms.IntegerField(
        error_messages={
            'required': '재고를 입력해주세요.'
        }, label='재고'
    )
    
    def clean(self):
        cd = super().clean() # cleaned_data
        name = cd.get('name') 
        price = cd.get('price')
        description = cd.get('description')
        stock = cd.get('stock')
        
        if name and price and description and stock:
            product = Product(
                name=name,
                price=price,
                description=description,
                stock=stock
            )
            product.save()