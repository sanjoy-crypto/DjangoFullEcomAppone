from django.db import models

# Create your models here.


class Category(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'),
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='category')
    status = models.CharField(max_length=20, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='product/')
    new_price = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    old_price = models.DecimalField(decimal_places=2, max_digits=15)
    amount = models.IntegerField(default=0)
    min_amount = models.IntegerField(default=3)
    detail = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Images(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='product/')

    def __str__(self):
        return self.title


class SliderImage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    bgimage = models.ImageField(blank=True, upload_to='slider/')
    price = models.DecimalField(decimal_places=2, max_digits=15, default=0)

    def __str__(self):
        return self.title


class RightImage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='slider/')

    def __str__(self):
        return self.title
