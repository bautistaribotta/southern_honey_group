from django.urls import path
from main.views import login, inicio, productos, clientes, deudores, remitos

"""
La sentencia name="nombre_del_archivo" se usa 
para que Django sepa la ruta relativa del .html
"""
urlpatterns = [
    path('', login, name="login"),
    path('inicio/', inicio, name="inicio"),
    path('productos/', productos, name="productos"),
    path('clientes/', clientes, name="clientes"),
    path('deudores/', deudores, name="deudores"),
    path('remitos/', remitos, name="remitos")
]