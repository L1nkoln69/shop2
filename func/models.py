from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.urls import reverse


class Profile(AbstractUser):
    avatar = models.ImageField(default='static/images/img.png')
    money = models.DecimalField(max_digits=100000000, decimal_places=0, default=0)


class Products(models.Model):
    product_type = (
       ('PC', 'Computer'),
       ('NB', 'NoteBook'),
       ('KB', 'KeyBoard'),
       ('M', 'Mouse'),
       ('S', 'Screen'),
       ('T', 'Table'),
       ('C', 'Chair')
    )

    currency = (
        ('$', 'dollar'),
        ('€', 'euro')
    )

    title = models.CharField(max_length=100)
    type_product = models.CharField(choices=product_type, max_length=2)
    image = models.ImageField()
    price = models.PositiveIntegerField()
    currency = models.CharField(choices=currency, max_length=1)
    amount = models.PositiveIntegerField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # basket = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("product", args=[str(self.id)])


class Reviews(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

