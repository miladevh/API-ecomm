from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='product_image/%Y/%m/')
    description = models.TextField()
    price = models.BigIntegerField()
    available = models.BooleanField(default=True)
    is_sale = models.BooleanField(default=False)
    discount_percent = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('home:product_details', kwargs={'pk':self.id})

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comment')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} {self.product.name}'