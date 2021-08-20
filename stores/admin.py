from django.contrib import admin
from .models import Products, ProductTypes, ProductPictures, Manufactures

admin.site.register(
    [Products, ProductTypes, ProductPictures, Manufactures]
)
