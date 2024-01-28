from django import forms
from .models import Images


class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image', 'is_logo', 'is_watermark']
