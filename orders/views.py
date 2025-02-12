from django.shortcuts import render, get_object_or_404
from orders.models import Order, OrderItem
from orders.forms import OrderCreatedForm, UserOrderDontLogIn
from cart.cart import Cart
from django.contrib.auth.models import User
from blog2.models import Profile

def order_created(request, user_id=None):
    cart = Cart(request)
    user = None
    profile = None
    
    if user_id:
        user = User.objects.get(id = user_id)
        profile = get_object_or_404(Profile, user = user)
        
    if request.method == 'POST':
        if user and user.is_authenticated:
            form = OrderCreatedForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = user
                order.profile = profile
                order.first_name = user.first_name
                order.last_name = user.last_name 
                order.email = user.email
                order.save()
        
                for item in cart:
                    OrderItem.objects.create(order=order, 
                                             product = item['product'], 
                                             price=item['price'], 
                                             quantity=item['quantity'])
                
                cart.clear()
                return render(request, 'orders/created.html', {'order': order})
            
        else:
            form_dont_login = UserOrderDontLogIn(request.POST)
            if form_dont_login.is_valid():
                order = form_dont_login.save()
                
                for item in cart:
                    OrderItem.objects.create(order=order, 
                                             product = item['product'], 
                                             price=item['price'], 
                                             quantity=item['quantity'])
                
                cart.clear()
                return render(request, 'orders/created.html', {'order': order})
                
            
    else:
        form = OrderCreatedForm() if user and user.is_authenticated else None
        form_dont_login = UserOrderDontLogIn() if not user or not user.is_authenticated else None
    
    context = {
        'cart': cart,
        'form': form,
        'user': user,
        'profile': profile,
        'form_dont_login': form_dont_login,
    }
    
    return render(request, 'orders/create.html', context)
