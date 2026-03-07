import requests
from bs4 import BeautifulSoup


def get_cotizacion_oficial_venta():
    url_dolar_oficial = "https://dolarapi.com/v1/dolares/oficial"
    try:
        respuesta = requests.get(url_dolar_oficial, verify=True)
        resp_json = respuesta.json()
        valor_dolar_oficial_venta = resp_json["venta"]
        return valor_dolar_oficial_venta
    except Exception as e:
        print(f"Error al obtener cotización oficial: {e}")
        return None


def get_cotizacion_blue_venta():
    url_dolar_blue = "https://dolarapi.com/v1/dolares/blue"
    try:
        respuesta = requests.get(url_dolar_blue, verify=True)
        resp_json = respuesta.json()
        valor_dolar_blue_venta = resp_json["venta"]
        return valor_dolar_blue_venta
    except Exception as e:
        print(f"Error al obtener cotización blue: {e}")
        return None


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
        print(f"Error al obtener cotización miel clara: {e}")
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
        print(f"Error al obtener cotización miel oscura: {e}")
        return None
