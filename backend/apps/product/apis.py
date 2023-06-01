from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from apps.product.selectors import product_list
from apps.api.pagination import LimitOffsetPagination, get_paginated_response
from apps.product.models import Product, Category, Brand, ProductType, Warrenty, Seller



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
            fields = ("id", "name", "image", "catagory", "product_type", "brand", "normal_sell_price", "discounted_sell_price", "warrenty", 'seller')

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
        name = serializers.CharField(required=False, allow_null=False, allow_blank=False)
        catagory = serializers.CharField(required=False, allow_null=False)
        product_type = serializers.CharField(required=False, allow_null=False, allow_blank=False)
        brand = serializers.CharField(required=False, allow_null=False, allow_blank=False)
        sell_price_min = serializers.IntegerField(required=False, allow_null=False, min_value=0)
        sell_price_max = serializers.IntegerField(required=False, allow_null=False, min_value=0)
        warrenty = serializers.CharField(required=False, allow_null=False, allow_blank=False)
        seller = serializers.CharField(required=False, allow_null=False, allow_blank=False)
        search = serializers.CharField(required=False, allow_null=False, allow_blank=False)


    def get(self, request):
        # client = request.query_params.get('client')
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        products = product_list(filters=filters_serializer.validated_data)

        # products = Product.objects.filter(catagory__name__in=['Headphone', 'Laptop', 'Phone'])

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=products,
            request=request,
            view=self,
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name")


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ("id", "name")


class WarrentySerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrenty
        fields = ("id", "name")


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ("id", "name")


class ProductFilterList(APIView):

    class OutputSerializer(serializers.Serializer):
        catagory_list = CategorySerializer(many=True)
        product_type_list = ProductTypeSerializer(many=True)
        brand_list = BrandSerializer(many=True)
        warrenty_list = WarrentySerializer(many=True)
        seller_list = SellerSerializer(many=True)

        class Meta:
            fields = ("catagory_list", "product_type_list", "brand_list", "warrenty_list", 'seller_list')

    def get(self, request):
        catagories = Category.objects.all()
        product_types = ProductType.objects.all()
        brands = Brand.objects.all()
        warrenties = Warrenty.objects.all()
        sellers = Seller.objects.all()
        data = {
            "catagory_list": catagories,
            "product_type_list": product_types,
            "brand_list": brands,
            "warrenty_list": warrenties,
            "seller_list": sellers
        }
        serializer = self.OutputSerializer(data)

        return Response(serializer.data, status=status.HTTP_200_OK)

