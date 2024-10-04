
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from .models import Category, Product
from .models import *
from .forms import *



def home(request):
    return render(request, 'home.html')


@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def menu(request, category_name=None):
    selected_category = request.GET.get('category', 'all')
    categories = Category.objects.all()
    if selected_category == 'all':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__id=selected_category)

    context = {
        'categories': categories,
        'products': products,
        'selected_category': selected_category
    }
    return render(request, 'menu.html', context)




@login_required
def bookings(request):
    if request.method == 'POST':
        result = FeedbackForm(request.POST)
        if result.is_valid():
            name = result.cleaned_data['name']
            email = result.cleaned_data['email']
            feedback = result.cleaned_data['feedback']
            result = Feedback(name=name, email=email, feedback=feedback)
            result.save()
            messages.info(request, 'Feedback submitted -- Thank you!')
        else:
            messages.error(request, 'Form is not valid, please correct the errors')

    return render(request, 'bookings.html', {})


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
        

    else:
        return render(request,'login.html')

def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name taken')
                return redirect('registration')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already registered')
                return redirect('registration')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save();
                print('user created')
                return redirect('login')
                
            
        else:
            messages.info(request,'password not matching..')
            return redirect('registration')
        
        
            
    else:
        return render(request, 'registration.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')

@login_required
def cart_view(request):
    return render(request, 'cart.html')





# @require_POST
# def add_to_cart(request, product_id):
#     # Get the cart from the session
#     cart = request.session.get('cart', {})

#     # Add product to cart or increment quantity
#     if product_id in cart:
#         cart[product_id] += 1
#     else:
#         cart[product_id] = 1

#     # Save the updated cart back into the session
#     request.session['cart'] = cart

#     # Optionally add a success message
#     messages.success(request, 'Product added to cart!')

#     return redirect('menu')

# @require_POST
# def update_cart(request, product_id):
#     action = request.POST.get('action')
#     cart = request.session.get('cart', {})

#     if product_id in cart:
#         if action == 'increment':
#             cart[product_id] += 1
#         elif action == 'decrement':
#             cart[product_id] -= 1
#             if cart[product_id] <= 0:
#                 del cart[product_id]  # Remove item if quantity is 0 or less

#         request.session['cart'] = cart
#         messages.success(request, 'Cart updated successfully!')

#     return redirect('menu')



# def cart(request):
#     cart = request.session.get('cart', {})
#     products = Product.objects.filter(id__in=cart.keys())
#     total_price = sum([product.price * cart[str(product.id)] for product in products])

#     context = {
#         'cart_items': cart,
#         'products': {product.id: product for product in products},
#         'total_price': total_price,
#     }
    
#     return render(request, 'cart.html', context)

# def cart_increment(request, product_id):
#     cart = request.session.get('cart', {})
#     cart[str(product_id)] = cart.get(str(product_id), 0) + 1
#     request.session['cart'] = cart
#     return redirect('cart')

# def cart_decrement(request, product_id):
#     cart = request.session.get('cart', {})
#     if cart.get(str(product_id), 0) > 1:
#         cart[str(product_id)] -= 1
#     else:
#         cart.pop(str(product_id), None)
#     request.session['cart'] = cart
#     return redirect('cart')

# def cart_remove(request, product_id):
#     cart = request.session.get('cart', {})
#     cart.pop(str(product_id), None)
#     request.session['cart'] = cart
#     return redirect('cart')