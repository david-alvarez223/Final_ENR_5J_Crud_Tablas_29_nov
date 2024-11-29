from django.urls import path
from inventory_app import views

urlpatterns = [
    path("Inventory",views.view_indexInventory,name="Inventory"),
    path("registerInventory/",views.registerInventory,name="registerInventory"),
    path("selectInventory/<inventory_id>",views.selectInventory,name="selectInventory"),
    path("selectInventory/editInventory/",views.editInventory,name="editInventory"),
    path("deleteInventory/<inventory_id>",views.deleteInventory,name="deleteInventory"),
]
