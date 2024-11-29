from django.shortcuts import render,redirect
from .models import Inventory

# Create your views here.
def view_indexInventory(request):
    inventory=Inventory.objects.all()
    return render(request,"inventory.html",{"inventory1":inventory})

def registerInventory(request):
    id=request.POST["txtid"]
    name=request.POST["txtname"]
    price=request.POST["numprice"]
    quantity=request.POST["numquantity"]
    type=request.POST["txttype"]

    saveInventory=Inventory.objects.create(inventory_id=id,inventory_name=name,inventory_capacity=price,inventory_quantity=quantity,type=type)#GUARDA EL REGISTRO

    return redirect("Inventory")

def selectInventory(request,inventory_id):
    inventory=Inventory.objects.get(inventory_id=inventory_id)
    return render(request,"editI.html",{"inventory1":inventory})

def editInventory(request):
    inventory_id=request.POST["txtid"]
    name=request.POST["txtname"]
    price=request.POST["numprice"]
    quantity=request.POST["numquantity"]
    type=request.POST["txttype"]
    inventory=Inventory.objects.get(inventory_id=inventory_id)
    inventory.inventory_name=name
    inventory.inventory_capacity=price
    inventory.inventory_quantity=quantity
    inventory.type=type
    
    inventory.save() # actualiza registros
    return redirect("Inventory")

def deleteInventory(request,inventory_id):
    inventory=Inventory.objects.get(inventory_id=inventory_id)
    inventory.delete() # borra el registro

    return redirect("Inventory")
