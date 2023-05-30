from django.db.models.query import QuerySet, Q
from apps.product.models import Product
from apps.product.filters import ProductFilter


# Selector's definition starts from here
def product_list(*, filters=None) -> QuerySet[Product]:
    filters = filters or {}
    keyword = filters.get('search')
    qs = None
    if keyword is not None:
        qs = Product.objects.filter(
            Q(name__icontains=keyword) | 
            Q(description__icontains=keyword) |
            Q(catagory__icontains=keyword)
        )
    else:
        qs = ProductFilter(filters, Product.objects.all().order_by('-id')).qs

    return qs