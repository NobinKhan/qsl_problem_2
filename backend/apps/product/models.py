from django.db import models

from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(verbose_name='Name', max_length=100, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return 'no_name-Category-{}'.format(self.id)


class ProductType(BaseModel):
    name = models.CharField(verbose_name='Name', max_length=100, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return 'no_name-productType-{}'.format(self.id)


class Brand(BaseModel):
    name = models.CharField(verbose_name='Name', max_length=100, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return 'no_name-brand-{}'.format(self.id)


class Warrenty(BaseModel):
    name = models.CharField(verbose_name='Name', max_length=100, null=True, blank=True)
    period = models.DurationField(verbose_name='Period', null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return 'no_name-warrenty-{}'.format(self.id)


class Seller(BaseModel):
    name = models.CharField(verbose_name='Name', max_length=100, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return 'no_name-seller-{}'.format(self.id)


class Product(BaseModel):
    name = models.CharField(verbose_name='Name', max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    image = models.ImageField(verbose_name='Image', null=True, blank=True)
    catagory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    normal_sell_price = models.DecimalField(verbose_name='Normal Sell Price', max_digits=19, decimal_places=4, default=0, null=True, blank=True)
    discounted_sell_price = models.DecimalField(verbose_name='Discounted Sell Price', max_digits=19, decimal_places=4, default=0, null=True, blank=True)
    warrenty = models.ForeignKey(Warrenty, on_delete=models.SET_NULL, null=True, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return 'no_name-product-{}'.format(self.id)

