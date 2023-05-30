import django_filters
from apps.product.models import Product


# Filter definition starts from here
class ProductFilter(django_filters.FilterSet):
    catagory = django_filters.CharFilter(lookup_expr='icontains', field_name='catagory__name')
    product_type = django_filters.CharFilter(lookup_expr='icontains', field_name='product_type__name')
    brand = django_filters.CharFilter(lookup_expr='icontains', field_name='brand__name')
    warrenty = django_filters.CharFilter(lookup_expr='icontains', field_name='warrenty__name')
    seller = django_filters.CharFilter(lookup_expr='icontains', field_name='seller__name')
    sell_price = django_filters.RangeFilter(field_name='discounted_sell_price')


    class Meta:
        model = Product
        fields = ('name', "catagory", "product_type", "brand", "warrenty", "seller", "sell_price")

