from django.shortcuts import render,redirect
from .models import Client
# Create your views here.
def view_indexClients(request):
    clients=Client.objects.all()
    return render(request,"clients.html",{"clients1":clients})

def registerClient(request):
    client_id=request.POST["txtid"]
    client_name=request.POST["txtname"]
    client_rating=request.POST["numrating"]

    saveClient=Client.objects.create(client_id=client_id,client_name=client_name,client_rating=client_rating)#GUARDA EL REGISTRO

    return redirect("Clients")

def selectClient(request,client_id):
    clients=Client.objects.get(client_id=client_id)
    return render(request,"editC.html",{"clients1":clients})

def editClient(request):
    client_id=request.POST["txtid"]
    client_name=request.POST["txtname"]
    client_rating=request.POST["numrating"]
    clients=Client.objects.get(client_id=client_id)
    clients.client_name=client_name
    clients.client_rating=client_rating
    
    clients.save() # actualiza registros
    return redirect("Clients")

def deleteClient(request,client_id):
    clients=Client.objects.get(client_id=client_id)
    clients.delete() # borra el registro

    return redirect("Clients")