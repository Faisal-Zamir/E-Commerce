from django.urls import path, include
from . import views
urlpatterns = [
<<<<<<< HEAD:myecom/store/urls.py
    path('', views.homepage , name="mystore"),
=======
    path('mystore/', views.homepage , name="mystore"),
>>>>>>> b999440cbba0527563db802bda572f307ebc3396:store/urls.py
    # path('product/<int:pk>', views.category_wise_products , name="cat_product"),
    path('product_detail/<int:pk>', views.product_detail , name="product_detail"),
    path('cart', views.cart , name="cart"),
    path('orders', views.orders , name="orders"),
    path('check-out', views.check_out , name="check_out"),


]
