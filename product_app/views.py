from django.shortcuts import render,redirect
from .models import Product

# Create your views here.
def view_indexProducts(request):
    products=Product.objects.all()
    return render(request,"index.html",{"products1":products})

def registerProduct(request):
    id=request.POST["txtid"]
    name=request.POST["txtname"]
    price=request.POST["numprice"]
    type=request.POST["txttype"]

    saveProduct=Product.objects.create(product_id=id,product_name=name,product_price=price,product_type=type)#GUARDA EL REGISTRO

    return redirect("Products")

def selectProduct(request,product_id):
    products=Product.objects.get(product_id=product_id)
    return render(request,"editP.html",{"products1":products})

def editProduct(request):
    product_id=request.POST["txtid"]
    name=request.POST["txtname"]
    price=request.POST["numprice"]
    type=request.POST["txttype"]
    products=Product.objects.get(product_id=product_id)
    products.product_name=name
    products.product_price=price
    products.product_type=type
    
    products.save() # actualiza registros
    return redirect("Products")

def deleteProduct(request,product_id):
    products=Product.objects.get(product_id=product_id)
    products.delete() # borra el registro

    return redirect("Products")
