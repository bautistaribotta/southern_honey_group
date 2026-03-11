from .services import get_cotizacion_oficial, get_cotizacion_blue, get_cotizacion_miel_clara, get_cotizacion_miel_oscura
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Producto, Cliente


def login(request):
    if request.method == "POST":
        usuario_ingresado = request.POST.get("user")
        password_ingresada = request.POST.get("password")

        # Autenticacion
        usuario_valido = authenticate(request, username=usuario_ingresado, password=password_ingresada)

        # Si es válido los redirijo, si no, envío el error por mensaje
        if usuario_valido is not None:
            auth_login(request, usuario_valido)
            return redirect("inicio")
        else:
            messages.error(request, "Usuario y/o contraseña incorrectos")
            return redirect("login")

    # Si no se realizo un POST, simplemente cargo la pagina
    return render(request, "login.html")


"""
Si un usuario anónimo (sin loguearse) quiere acceder a las paginas internas, 
le bloqueo el acceso y lo envio de vuelta a '/' (pagina configurada del inicio del server) 
para que se loguee. Todo esto implementado usando el wrapped @login_required
"""


@login_required(login_url='/')
def inicio(request):
    dolar_oficial = get_cotizacion_oficial()
    dolar_blue = get_cotizacion_blue()
    contexto = {
        "oficial": dolar_oficial,
        "blue": dolar_blue
    }
    return render(request, "inicio.html", contexto)


@login_required(login_url='/')
def productos(request):
    # Trae todos los productos de la base de datos ordenados por nombre.
    productos = Producto.objects.all().order_by("nombre")

    # Divide esa lista total en bloques de 5 productos
    paginator_productos = Paginator(productos, 5)

    # Se fija en la URL en qué página está el usuario
    pagina_numero = request.GET.get("page")

    # Extraigo únicamente los 5 productos que corresponden a esa página específica
    pagina_obj = paginator_productos.get_page(pagina_numero)

    return render(request, "productos.html", {"productos":pagina_obj})


@login_required(login_url='/')
def clientes(request):
    """
    Repito el proceso aplicado en productos
    Query + Cant. pag. a mostrar + URL + Los 5 que corresponden + Enviar el listado al HTML
    """
    clientes = Cliente.objects.all().order_by("nombre")
    paginator_clientes = Paginator(clientes, 5)
    pagina_numero = request.GET.get("page")
    pagina_obj = paginator_clientes.get_page(pagina_numero)

    return render(request, "clientes.html", {"clientes": pagina_obj})


@login_required(login_url='/')
def deudores(request):
    return render(request, "deudores.html")


@login_required(login_url='/')
def remitos(request):
    return render(request, "remitos.html")


def cerrar_sesion(request):
    auth_logout(request)
    return redirect("login")