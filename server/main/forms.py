from django import forms


class ImageUploadForm(forms.Form):
    images = forms.FileField(required=True, widget=forms.ClearableFileInput(attrs={'multiple': True}))
