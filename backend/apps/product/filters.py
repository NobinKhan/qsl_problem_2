import django_filters
from apps.product.models import Product


# Filter definition starts from here
class ProductFilter(django_filters.FilterSet):
    # generic = django_filters.CharFilter(field_name='generic_name')
    # supplier = django_filters.CharFilter(field_name='supplier_Name')

    class Meta:
        model = Product
        fields = ('name', "catagory", "product_type", "brand", "warrenty", "seller", "discounted_sell_price")

