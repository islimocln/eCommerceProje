# cart/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import CartItem

@login_required
def cart_detail(request):
    # Kullanıcının sepetindeki ürünleri al
    cart_items = CartItem.objects.filter(cart__user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/cart_detail.html', context)

@login_required
def cart_add(request, product_id):
    # Sepete ürün ekleme işlemleri...
    pass

@login_required
def cart_remove(request, cart_item_id):
    # Sepetten ürün çıkarma işlemleri...
    pass
from django.shortcuts import render

def cart_detail(request):
    # Sepet verilerini buraya ekleyebilirsiniz.
    return render(request, 'cart/cart_detail.html')
from django.shortcuts import render

def cart_detail(request):
    # Sepet örneği (örnek veri)
    cart_items = [
        {
            "product": {
                "name": "Ürün 1",
                "description": "Bu bir ürün açıklamasıdır.",
                "price": 199,
                "image_url": "/static/img/sample-product.jpg",
            },
            "quantity": 2,
        },
        {
            "product": {
                "name": "Ürün 2",
                "description": "Başka bir ürün açıklaması.",
                "price": 299,
                "image_url": "/static/img/sample-product2.jpg",
            },
            "quantity": 1,
        },
    ]

    total_price = sum(item["product"]["price"] * item["quantity"] for item in cart_items)

    return render(request, "cart/cart_detail.html", {
        "cart_items": cart_items,
        "total_price": total_price,
    })

