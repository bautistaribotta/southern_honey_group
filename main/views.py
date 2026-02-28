from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, "login.html")

"""
Si un usuario anónimo quiere entrar a '/inicio/', bloqueo el acceso y
lo envio de vuelta a '/' (pagina configurada del inicio del server) para que se loguee
"""
@login_required(login_url='/')
def inicio(request):
    return render(request, "inicio.html")