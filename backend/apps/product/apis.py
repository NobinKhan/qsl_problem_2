from rest_framework import serializers
from rest_framework.views import APIView

from apps.product.models import Product
from apps.product.selectors import product_list
from apps.api.pagination import LimitOffsetPagination, get_paginated_response



# Api's definition starts from here
class ProductList(APIView):

    class Pagination(LimitOffsetPagination):
        default_limit = 20
        max_limit = 50


    class OutputSerializer(serializers.ModelSerializer):
        catagory = serializers.SerializerMethodField(read_only=True)
        product_type = serializers.SerializerMethodField(read_only=True)
        brand = serializers.SerializerMethodField(read_only=True)
        warrenty = serializers.SerializerMethodField(read_only=True)
        seller = serializers.SerializerMethodField(read_only=True)

        class Meta:
            model = Product
            fields = ("id", "name", "description", "image", "catagory", "product_type", "brand", "normal_sell_price", "discounted_sell_price", "warrenty", 'seller')

        def get_catagory(self, attb):
            if attb.catagory:
                return attb.catagory.name
            return None


        def get_product_type(self, attb):
            if attb.product_type:
                return attb.product_type.name
            return None

        def get_brand(self, attb):
            if attb.brand:
                return attb.brand.name
            return None

        def get_warrenty(self, attb):
            if attb.warrenty:
                return attb.warrenty.name
            return None

        def get_seller(self, attb):
            if attb.seller:
                return attb.seller.name
            return None


    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False, allow_null=False)
        name = serializers.CharField(required=False, allow_null=False, allow_blank=False)
        catagory = serializers.CharField(required=False, allow_null=False, allow_blank=False)
        product_type = serializers.CharField(required=False, allow_null=False, allow_blank=False)
        brand = serializers.CharField(required=False, allow_null=False, allow_blank=False)
        normal_sell_price = serializers.CharField(required=False, allow_null=False, allow_blank=False)


    def get(self, request):
        # client = request.query_params.get('client')
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        prducts = product_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=prducts,
            request=request,
            view=self,
        )

