from bs4 import BeautifulSoup
import requests
import json
import os.path
data = {}
data['Productos'] = []

url="https://listado.mercadolibre.cl/camara-seguridad"
r = requests.get(url)

soup= BeautifulSoup(r.content)

precio= soup.find_all('span',class_='price__fraction')
for precios in precio:
        print(precios.text)
        pass

nombre= soup.find_all('span',class_='main-title')
for nombres in nombre:
        print(nombres.text)
        pass
        
region= soup.find_all('div',class_='item__condition')
for regiones in region:
        print(regiones.text)
        pass
cuo= soup.find_all('div',class_='stack_column_item installments highlighted')
for cuotas in cuo:
        print(cuotas.text)
        pass 
        data['Productos'].append({
        'pagina': soup.title.string,
        'nombres':  nombres.text,
        'precios': precios.text,
        'vendidos': regiones.text,
        'cuotas': cuotas.text,
                                    })   
                  


dir = os.path.dirname(os.path.abspath(__file__)) + '/data'

file_name = "datos.json"
with open(os.path.join(dir, file_name), 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

data = {}
data['Productos'] = []



    