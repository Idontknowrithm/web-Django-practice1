from django import forms
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.Form):
    user_id = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=64, label='아이디'
    )
    user_name = forms.CharField(
        error_messages={
            'required': '이름을 입력해주세요.'
        },
        max_length=64, label='이름'
    )
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, max_length=64, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 확인해주세요.'
        },
        widget=forms.PasswordInput, max_length=64, label='비밀번호 확인'
    )
    
    def clean(self):
        cd = super().clean() # cleaned_data
        user_id = cd.get('user_id')
        user_name = cd.get('user_name')
        email = cd.get('email')
        password = cd.get('password')
        re_password = cd.get('re_password')
        
        if password and re_password:
            if password != re_password:
                self.add_error('re_password', '비밀번호를 다시 확인해주세요')
            else:
                user = User(
                    user_id=user_id,
                    user_name=user_name,
                    email=email,
                    password=make_password(password)
                )
                user.save()
                
class LoginForm(forms.Form):
    user_id = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=64, label='아이디'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, max_length=64, label='비밀번호'
    )
    
    def clean(self):
        cd = super().clean() # cleaned_data
        user_id = cd.get('user_id')
        password = cd.get('password')
        
        if user_id and password:
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                self.add_error('user_id', '아이디가 없습니다')
                return
            
            if not check_password(password, user.password):
                self.add_error('password', '비밀번호를 틀렸습니다')
            else:
                self.user_id = user_id
    