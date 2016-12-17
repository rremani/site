from django import forms
from django.contrib.auth import password_validation


class LoginForm(forms.Form):
    email = forms.CharField(label='Email', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))


class SignUpForm(forms.Form):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }

    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    password_f = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))
    password_s = forms.CharField(label='Repeat Password', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))

    def clean_password_s(self):
        password1 = self.cleaned_data.get("password_f")
        password2 = self.cleaned_data.get("password_s")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        # username = self.cleaned_data.get('username')
        password_validation.validate_password(self.cleaned_data.get('password_s'))
        return password2


class ImageUploadForm(forms.Form):
    image = forms.FileField(required=True)


class FolderUploadForm(forms.Form):
    image_folder = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'webkitdirectory': True,
                                                                        'directory': True}))
