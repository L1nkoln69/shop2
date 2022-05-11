from django.contrib import admin
from .models import Products, Reviews, Profile


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
