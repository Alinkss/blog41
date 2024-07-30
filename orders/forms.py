from django import forms
from orders.models import Order, OrderItem

class OrderCreatedForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['adress',]
        exclude = ('created', 'updated', 'paid', 'user', 'profile',)
        
class UserOrderDontLogIn(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'adress',]
        
        