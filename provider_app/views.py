from django.shortcuts import render,redirect
from .models import Provider

# Create your views here.
def view_indexProviders(request):
    providers=Provider.objects.all()
    return render(request,"providers.html",{"providers1":providers})

def registerProvider(request):
    id=request.POST["txtid"]
    name=request.POST["txtname"]
    dir=request.POST["txtdir"]

    saveProvider=Provider.objects.create(provider_id=id,provider_name=name,provider_dir=dir)#GUARDA EL REGISTRO

    return redirect("Providers")

def selectProvider(request,provider_id):
    providers=Provider.objects.get(provider_id=provider_id)
    return render(request,"editPR.html",{"providers1":providers})

def editProvider(request):
    id=request.POST["txtid"]
    name=request.POST["txtname"]
    dir=request.POST["txtdir"]
    providers=Provider.objects.get(provider_id=id)
    providers.provider_name=name
    providers.provider_dir=dir
    
    providers.save() # actualiza registros
    return redirect("Providers")

def deleteProvider(request,provider_id):
    providers=Provider.objects.get(provider_id=provider_id)
    providers.delete() # borra el registro

    return redirect("Providers")
