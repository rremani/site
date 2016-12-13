from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username / Email', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))


class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    password_f = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))
    password_s = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))


class ImageUploadForm(forms.Form):
    images = forms.FileField(required=True, widget=forms.ClearableFileInput(attrs={'multiple': True}))
