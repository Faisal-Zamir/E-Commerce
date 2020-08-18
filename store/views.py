from django.shortcuts import render, redirect
from . models import Product, Category, Order
from user.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def homepage(request):
    if request.method=='POST':
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
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
    else:
        pass

    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    categories  =  Category.objects.all()
    # user_data = Profile.objects.get(user_id=request.user.id)
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
    if request.session['cart'] == {}:
        return render(request, 'store/no_item.html')
    else:
        ids = list(request.session.get('cart').keys())
        print(ids)
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'store/cart.html',{'products' : products})

@login_required
def orders(request):
    orders = Order.objects.filter(user_id=request.user.id)
    print(orders)
    return render(request, 'store/orders.html',{'orders' : orders})


@login_required
def check_out(request):
    if request.method=='POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
    
        cart = request.session.get('cart')
        product_list = list(cart.keys())
        products = Product.get_products_by_id(product_list)

        for product in products:
            print(product)
            print(cart.get(str(product.id)))
            order = Order(user_id=request.user.id,
                            product=product,
                            price=product.price,
                            address=address,
                            phone=phone,
                            quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')
    else:
        return redirect('cart')
