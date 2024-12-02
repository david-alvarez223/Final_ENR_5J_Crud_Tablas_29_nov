from django.urls import path
from clients_app import views

urlpatterns = [
    path("Clients",views.view_indexClients,name="Clients"),
    path("registerClient/",views.registerClient,name="registerClients"),
    path("selectClient/<client_id>",views.selectClient,name="selectClient"),
    path("selectClient/editClient/",views.editClient,name="editClient"),
    path("deleteClient/<client_id>",views.deleteClient,name="deleteClient"),
]
