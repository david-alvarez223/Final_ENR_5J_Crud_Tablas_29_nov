from django.urls import path
from cafe_app import views

urlpatterns = [
    path("Cafe",views.view_indexCafe,name="Cafe"),
    path("registerCafe/",views.registerCafe,name="registerCafe"),
    path("selectCafe/<cafe_id>",views.selectCafe,name="selectCafe"),
    path("selectCafe/editCafe/",views.editCafe,name="editCafe"),
    path("deleteCafe/<cafe_id>",views.deleteCafe,name="deleteCafe"),
]
