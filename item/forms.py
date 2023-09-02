from django import forms

from .models import items

class NewItemForm(forms.ModelForm):
    class Meta:
        model = items
        fields = ('category', 'name', 'description', 'price', 'image',)
