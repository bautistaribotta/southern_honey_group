import requests
from bs4 import BeautifulSoup


def get_cotizacion_oficial():
    url_dolar_oficial = "https://dolarapi.com/v1/dolares/oficial"
    try:
        respuesta = requests.get(url_dolar_oficial, verify=True)
        datos = respuesta.json()
        return {
            "compra": datos.get("compra"),
            "venta": datos.get("venta")
        }
    except Exception as e:
        print(f"Error al obtener cotización oficial: {e}") # Quitar a futuro
        return {
            "compra": None,
            "venta": None
        }


def get_cotizacion_blue():
    url_dolar_blue = "https://dolarapi.com/v1/dolares/blue"
    try:
        respuesta = requests.get(url_dolar_blue, verify=True)
        datos = respuesta.json()
        return {
            "compra": datos.get("compra"),
            "venta": datos.get("venta")
        }
    except Exception as e:
        print(f"Error al obtener cotización oficial: {e}")  # Quitar a futuro
        return {
            "compra": None,
            "venta": None
        }


def get_cotizacion_miel_clara():
    url = r"https://infomiel.com/"
    try:
        respuesta = requests.get(url)
        html_resp = respuesta.text
        soup = BeautifulSoup(html_resp, "html.parser")
        todas_las_etiquetas = soup.find_all("td")
        precio_miel_clara = todas_las_etiquetas[0].text
        
        miel_clara_limpia = "".join(filter(str.isdigit, precio_miel_clara))
        return miel_clara_limpia
    except Exception as e:
        print(f"Error al obtener cotización miel clara: {e}") # Quitar a futuro
        return None


def get_cotizacion_miel_oscura():
    url = r"https://infomiel.com/"
    try:
        respuesta = requests.get(url)
        html_resp = respuesta.text
        soup = BeautifulSoup(html_resp, "html.parser")
        todas_las_etiquetas = soup.find_all("td")
        precio_miel_oscura = todas_las_etiquetas[1].text
        
        miel_oscura_limpia = "".join(filter(str.isdigit, precio_miel_oscura))
        return miel_oscura_limpia
    except Exception as e:
        print(f"Error al obtener cotización miel oscura: {e}") # Quitar a futuro
        return None


def nuevo_producto(nombre, categoria=None, precio=None, cantidad=None):
    from .models import Producto
    nuevo_producto = Producto.objects.create(
                    nombre=nombre,
                    categoria=categoria,
                    precio=precio,
                    cantidad=cantidad
    )
    return nuevo_producto


def nuevo_cliente(nombre, apellido=None, telefono=None, localidad=None, direccion=None, cuit=None, factura_produccion=False):
    from .models import Cliente
    nuevo_cliente = Cliente.objects.create(
                    nombre=nombre,
                    apellido=apellido,
                    telefono=telefono,
                    localidad=localidad,
                    direccion=direccion,
                    cuit=cuit,
                    factura_produccion=factura_produccion
    )
    return nuevo_cliente
