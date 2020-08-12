from django.shortcuts import render, redirect
from . models import Product, Category
from user.models import Profile
from django.contrib.auth.models import User

def homepage(request):

    categories  =  Category.objects.all()
    user_data = Profile.objects.get(user_id=request.user.id)
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
        'user_data':user_data
        }
    return render(request, 'store/index.html',context)

def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    
    context = {'product':product}
    return render(request, 'store/product_detail.html',context)

 