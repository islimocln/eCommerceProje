from django.db import models
from django.contrib.auth.models import User


# Product Modeli
class Product(models.Model):
    name = models.CharField(max_length=255)  # Ürün adı
    description = models.TextField()  # Ürün açıklaması
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Ürün fiyatı
    stock = models.PositiveIntegerField()  # Stok miktarı
    category = models.CharField(max_length=100)  # Ürün kategorisi
    image_url = models.URLField(blank=True, null=True)  # Ürün resmi URL'si
    features = models.JSONField(blank=True, null=True)  # Ürün özellikleri
    created_at = models.DateTimeField(auto_now_add=True)  # Ürünün eklenme zamanı

    def __str__(self):
        return self.name


# History Modeli (Satın Alma Geçmişi)
class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="histories")  # Kullanıcı ile ilişki
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="histories")  # Ürün ile ilişki
    quantity = models.PositiveIntegerField()  # Satın alınan ürün adedi
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Toplam fiyat
    purchase_date = models.DateTimeField(auto_now_add=True)  # Satın alma zamanı

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.purchase_date}"
