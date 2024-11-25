from django.shortcuts import render,redirect
from .models import Product

# Create your views here.
def view_indexProducts(request):
    products=Product.objects.all()
    return render(request,"index.html",{"products":products})

def registerProduct(request):
    id=request.POST["txtid"]
    name=request.POST["txtname"]
    price=request.POST["numprice"]

    saveProduct=Product.objects.create(product_id=id,product_name=name,product_price=price)#GUARDA EL REGISTRO

    return redirect("Products")

def selectProduct(request,id):
    products=Product.objects.get(product_id=id)
    return render(request,"editProduct.html",{"products":products})

def editProduct(request):
    products=Product.objects.get(product_id=id)
    products.product_name=name
    products.product_price=price
    id=request.POST["txtid"]
    name=request.POST["txtname"]
    price=request.POST["numprice"]
    Product.save() # actualiza registros
    return redirect("Products")

def deleteProduct(request,id):
    products=Product.objects.get(product_id=id)
    products.delete() # borra el registro

    return redirect("Products")
