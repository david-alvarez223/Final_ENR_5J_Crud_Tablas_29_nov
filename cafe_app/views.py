from django.shortcuts import render,redirect
from .models import Cafe

# Create your views here.
def view_indexCafe(request):
    cafe=Cafe.objects.all()
    return render(request,"cafe.html",{"cafe1":cafe})

def registerCafe(request):
    id=request.POST["txtid"]
    name=request.POST["txtname"]
    price=request.POST["numprice"]
    man=request.POST["txtman"]
    phone=request.POST["txtphone"]
    city=request.POST["txtcity"]
    mail=request.POST["txtmail"]

    saveCafe=Cafe.objects.create(cafe_id=id,cafe_dir=name,cafe_num=price,cafe_man=man,cafe_phone=phone,cafe_city=city,cafe_mail=mail)#GUARDA EL REGISTRO

    return redirect("Cafe")

def selectCafe(request,cafe_id):
    cafe=Cafe.objects.get(cafe_id=cafe_id)
    return render(request,"editCA.html",{"cafe1":cafe})

def editCafe(request):
    cafe_id=request.POST["txtid"]
    name=request.POST["txtname"]
    price=request.POST["numprice"]
    man=request.POST["txtman"]
    phone=request.POST["txtphone"]
    city=request.POST["txtcity"]
    mail=request.POST["txtmail"]
    cafe=Cafe.objects.get(cafe_id=cafe_id)
    cafe.cafe_dir=name
    cafe.cafe_num=price
    cafe.cafe_man=man
    cafe.cafe_phone=phone
    cafe.cafe_city=city
    cafe.cafe_mail=mail
    
    cafe.save() # actualiza registros
    return redirect("Cafe")

def deleteCafe(request,cafe_id):
    cafe=Cafe.objects.get(cafe_id=cafe_id)
    cafe.delete() # borra el registro

    return redirect("Cafe")
