from bs4 import BeautifulSoup
import requests
import json
import os.path
data = {}
data['Productos'] = []

url="https://listado.mercadolibre.cl/camara-seguridad"
r = requests.get(url)

soup= BeautifulSoup(r.content)


for b in range(1,50):
        nombre= soup.find_all('span',class_='main-title')[b]
        precio= soup.find_all('span',class_='price__fraction')[b]
        region= soup.find_all('div',class_='item__condition')[b]
        cuo= soup.find_all('div',class_='stack_column_item installments highlighted')[b]

        data['Productos'].append({
        'pagina': soup.title.string,
        'nombres':  nombre.text,
        'precios': precio.text,
        'vendidos': region.text,
        'cuotas': cuo.text,
                                    })   
        pass
print("json Creado!")
dir = os.path.dirname(os.path.abspath(__file__)) + '/data'

file_name = "datos.json"
with open(os.path.join(dir, file_name), 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

data = {}
data['Productos'] = []



    