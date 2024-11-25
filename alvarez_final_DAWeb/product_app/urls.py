from django.urls import path
from product_app import views

urlpatterns = [
    path("Products",views.view_indexProducts,name="Products"),
    path("registerProduct/",views.registerProduct,name="registerProduct"),
    path("selectProduct/<codigo>",views.selectProduct,name="selectProduct"),
    path("editProduct/",views.editProduct,name="editProduct"),
    path("deleteProduct/<codigo>",views.deleteProduct,name="deleteProduct"),
]
