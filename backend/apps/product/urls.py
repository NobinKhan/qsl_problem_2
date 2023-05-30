from django.urls import path

from apps.product.apis import ProductList, ProductFilterList



urlpatterns = [
    path("list/", ProductList.as_view()),
    path("filter/list/", ProductFilterList.as_view()),
]

