from django.shortcuts import render, redirect
from . models import Product, Category, Order
from user.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def homepage(request):
    if request.method == "POST":
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            print(product)
            cart[product] = 1
        request.session['cart'] = cart
        print('cart' , request.session['cart'])

    else:
        pass

    categories  =  Category.objects.all()
    products = None
    categoryID = request.GET.get('category')
    categoryID
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.objects.all()
    
    # count_cat_product = Product.objects.filter(category_id=categoryID).count()

    context = {
        'products':products,
        'categories':categories,
        
        }
    return render(request, 'store/index.html',context)

def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    
    context = {'product':product}
    return render(request, 'store/product_detail.html',context)



def cart(request):
    ids = list(request.session.get('cart').keys())
    # ak list aa jygi jismain product ki id's hungi or wo list ky zairy filter krngy
    products = Product.get_products_by_id(ids)
    #print(products)

    return render(request, 'store/cart.html', {'products' : products})

@login_required(login_url='/login')
def orders(request):
    returnUrl = request.META['PATH_INFO']
    print(request.META['PATH_INFO'])
    user =  request.session.get('user')
    #print(user)
    orders = Order.get_orders_by_user(user)
    #print(orders)
    return render(request, 'store/orders.html', {'orders' : orders})

def check_out(request):
    if request.method == "POST":
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(user=request.user,
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')

    return render(request, 'store/cart.html')
