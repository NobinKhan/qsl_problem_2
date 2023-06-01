import django_filters
from apps.product.models import Product


# Filter definition starts from here
class ProductFilter(django_filters.FilterSet):
    catagory = django_filters.CharFilter(field_name='catagory__name', method='filter_catagory')
    product_type = django_filters.CharFilter(method='filter_product_type', field_name='product_type__name')
    brand = django_filters.CharFilter(method='filter_brand', field_name='brand__name')
    warrenty = django_filters.CharFilter(method='filter_warrenty', field_name='warrenty__name')
    seller = django_filters.CharFilter(method='filter_seller', field_name='seller__name')
    sell_price = django_filters.RangeFilter(field_name='discounted_sell_price')

    def filter_catagory(self, queryset, name, value):
        categories = value.split(',')  # Split the comma-separated values
        return queryset.filter(catagory__name__in=categories)

    def filter_product_type(self, queryset, name, value):
        product_types = value.split(',')  # Split the comma-separated values
        return queryset.filter(product_type__name__in=product_types)

    def filter_brand(self, queryset, name, value):
        brands = value.split(',')  # Split the comma-separated values
        return queryset.filter(brand__name__in=brands)

    def filter_warrenty(self, queryset, name, value):
        warrentys = value.split(',')  # Split the comma-separated values
        return queryset.filter(warrenty__name__in=warrentys)

    def filter_seller(self, queryset, name, value):
        sellers = value.split(',')  # Split the comma-separated values
        return queryset.filter(seller__name__in=sellers)


    class Meta:
        model = Product
        fields = ('name', "catagory", "product_type", "brand", "warrenty", "seller", "sell_price")

