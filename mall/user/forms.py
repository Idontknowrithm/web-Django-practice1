from django import forms

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
        
        if password and re_password :
            if password != re_password:
                self.add_error('re_password', '비밀번호를 다시 확인해주세요')
            else:
                user = User(
                    user_id=user_id,
                    user_name=user_name,
                    email=email,
                    password=password
                )
                user.save()
    