
from django.shortcuts import render
from .mongodb import get_mongo_client

def product_list(request):
    # MongoDB'den ürünleri çek
    products_collection = get_mongo_client()
    raw_products = list(products_collection.find())  # MongoDB'deki tüm ürünleri al

    # Anahtarları düzenle
    products = []
    for product in raw_products:
        products.append({
            "product_name": product.get("product_name", ""),
            "image_link": product.get("image_link", ""),
            "price_dollar": product.get("Price (Dollar)", 0),  # Price (Dollar) düzenlendi
            "model_name": product.get("model_name", ""),       # model_name düzenlendi
        })

    return render(request, "products/product_list.html", {"products": products})
