from django.urls import path
from provider_app import views

urlpatterns = [
    path("Providers",views.view_indexProviders,name="Providers"),
    path("registerProvider/",views.registerProvider,name="registerProvider"),
    path("selectProvider/<provider_id>",views.selectProvider,name="selectProvider"),
    path("selectProvider/editProvider/",views.editProvider,name="editProvider"),
    path("deleteProvider/<provider_id>",views.deleteProvider,name="deleteProvider"),
]
