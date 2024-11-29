from django.urls import path
from employees_app import views

urlpatterns = [
    path("Employees",views.view_indexEmployees,name="Employees"),
    path("registerEmployee/",views.registerEmployee,name="registerEmployee"),
    path("selectEmployee/<employee_id>",views.selectEmployee,name="selectEmployee"),
    path("selectEmployee/editEmployee/",views.editEmployee,name="editEmployee"),
    path("deleteClient/<employee_id>",views.deleteEmployee,name="deleteEmployee"),
]
