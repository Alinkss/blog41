from django import forms
from shop.models import Product


# PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,21)]

class CartAddForm(forms.Form):
    def __init__(self, *args, **kwargs):
        product = kwargs.pop('product', None)
        super(CartAddForm, self).__init__( *args, **kwargs)
        
        if product:
            avaible_quantity = product.stock
            self.fields['quantity'].choices = [(i, str(i)) for i in range(1, avaible_quantity + 1)]
            
    quantity = forms.TypedChoiceField(coerce=int)
    update = forms.BooleanField(required= False, initial= False, widget= forms.HiddenInput)
    
    
