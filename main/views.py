from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, "login.html")


"""
Si un usuario anónimo (sin loguearse) quiere acceder a las paginas internas, 
le bloqueo el acceso y lo envio de vuelta a '/' (pagina configurada del inicio del server) 
para que se loguee. Todo esto implementado usando el wrapped @login_required
"""


@login_required(login_url='/')
def inicio(request):
    return render(request, "inicio.html")


@login_required(login_url='/')
def productos(request):
    return render(request, "productos.html")


@login_required(login_url='/')
def clientes(request):
    return render(request, "clientes.html")


@login_required(login_url='/')
def deudores(request):
    return render(request, "deudores.html")

@login_required(login_url='/')
def remitos(request):
    return render(request, "remitos.html")