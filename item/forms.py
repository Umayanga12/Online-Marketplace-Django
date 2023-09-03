from django import forms
from .models import items


#adding the fields to the form 
class NewItemForm(forms.ModelForm):
    class Meta:
        model = items
        fields = {'item_cat', 'name', 'discription', 'price', 'item_img', }


