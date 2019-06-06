from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label=("用户名"))
    passwd = forms.CharField(label=("密码"), widget=forms.PasswordInput)
    email = forms.EmailField(label=("邮箱"))
class LoginForm(forms.Form):
    username = forms.CharField(label=("用户名"))
    passwd = forms.CharField(label=("密码"), widget=forms.PasswordInput)