from django.urls import path
from product_app import views

urlpatterns = [
    path("Products",views.view_indexProducts,name="Products"),
    path("registerProduct/",views.registerProduct,name="registerProduct"),
    path("selectProduct/<product_id>",views.selectProduct,name="selectProduct"),
    path("selectProduct/editProduct/",views.editProduct,name="editProduct"),
    path("deleteProduct/<product_id>",views.deleteProduct,name="deleteProduct"),
]
