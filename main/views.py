from .services import (get_cotizacion_oficial, get_cotizacion_blue,
                       get_cotizacion_miel_clara, get_cotizacion_miel_oscura,
                       nuevo_producto, nuevo_cliente)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Producto, Cliente


def login(request):
    if request.method == "POST":
        usuario = request.POST.get("user")
        password = request.POST.get("password")

        # Autenticacion
        usuario_valido = authenticate(request, username=usuario, password=password)

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


@login_required
def inicio(request):
    dolar_oficial = get_cotizacion_oficial()
    dolar_blue = get_cotizacion_blue()
    contexto = {
        "oficial": dolar_oficial,
        "blue": dolar_blue
    }
    return render(request, "inicio.html", contexto)


@login_required
def productos(request):
    # Recibo el metodo POST, guardo los datos del formulario, creo
    # el producto en la base de datos, queda realizar validaciones
    if request.method == "POST":
        nombre_producto = request.POST.get("nombre")
        categoria = request.POST.get("categoria")
        precio = request.POST.get("precio")
        cantidad = request.POST.get("stock")

        nuevo_producto(nombre_producto, categoria, precio, cantidad)
        messages.success(request, "Producto agregado correctamente.")

        return redirect("productos")

    # Trae solo los productos activos de la base de datos ordenados por nombre.
    productos = Producto.objects.filter(activo=True).order_by("nombre")

    # Divide esa lista total en bloques de 5 productos
    paginator_productos = Paginator(productos, 5)

    # Se fija en la URL en qué página está el usuario
    pagina_numero = request.GET.get("page")

    # Extraigo únicamente los 5 productos que corresponden a esa página específica
    pagina_obj = paginator_productos.get_page(pagina_numero)

    return render(request, "productos.html", {"productos":pagina_obj})


@login_required
def clientes(request):
    if request.method == "POST":
        nombre_cliente = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        telefono = request.POST.get("telefono")
        localidad = request.POST.get("localidad")
        direccion = request.POST.get("direccion")
        factura = request.POST.get("factura")
        cuit = request.POST.get("cuit")

        nuevo_cliente(nombre_cliente, apellido, telefono, localidad, direccion, factura, cuit)
        messages.success(request, "Cliente creado correctamente")

        return redirect("clientes")

    """
    Repito el proceso aplicado en productos
    Query + Cant. pag. a mostrar + URL + Los 5 que corresponden + Enviar el listado al HTML
    """
    # Trae solo los clientes activos de la base de datos ordenados por nombre.
    clientes = Cliente.objects.filter(activo=True).order_by("nombre")
    paginator_clientes = Paginator(clientes, 5)
    pagina_numero = request.GET.get("page")
    pagina_obj = paginator_clientes.get_page(pagina_numero)

    return render(request, "clientes.html", {"clientes": pagina_obj})


@login_required
def deudores(request):
    return render(request, "deudores.html")


@login_required
def remitos(request):
    return render(request, "remitos.html")


def cerrar_sesion(request):
    auth_logout(request)
    return redirect("login")