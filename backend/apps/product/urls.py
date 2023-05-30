from django.urls import path

from apps.product.apis import ProductList



urlpatterns = [
    path("list/", ProductList.as_view()),
]

