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

    saveProduct=Product.objects.create(product_id=id,product_name=name,product_price=price)#GUARDA EL REGISTRO

    return redirect("Products")

def selectProduct(request,product_id):
    products=Product.objects.get(product_id=product_id)
    return render(request,"editP.html",{"products1":products})

def editProduct(request):
    product_id=request.POST["txtid"]
    name=request.POST["txtname"]
    price=request.POST["numprice"]
    products=Product.objects.get(product_id=product_id)
    products.product_name=name
    products.product_price=price
    
    products.save() # actualiza registros
    return redirect("Products")

def deleteProduct(request,product_id):
    products=Product.objects.get(product_id=product_id)
    products.delete() # borra el registro

    return redirect("Products")
