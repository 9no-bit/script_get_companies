import requests
from constants import URL, fileJson
from bs4 import BeautifulSoup
import time
import json

print(":::::Iniciando proceso:::::")

response = requests.get(URL)
resources = dict()

if response.status_code == 200:
  ## exito
  print("Datos obtenidos:")
  sopa = BeautifulSoup(response.text, 'html.parser')
  lista = sopa.find(class_='operators-list')
  elements = lista.find_all("li")
  for el in elements:
    name = el.get('data-name')
    els = el.select("div.accordion-body > a")
    if len(els) > 0:
      for e in els:
        url = e.get('href')
        name = e.text
        if url in resources:
          c = resources[url]
          c.append(name)
          resources[url] = c
        else:
          resources[url] = [name]
    else:
      url = el.find('a').get('href')
      if url in resources:
        c = resources[url]
        c.append(name)
        resources[url] = c
      else:
        resources[url] = [name]
else:
  ## error
  print("Error:", response.status_code)

data = json.dumps(dict(version=int(time.time()), companies=resources))

## CREAR ARCHIVO JSON ##
with open(fileJson, "w") as archivo:
    archivo.write(data)

print(":::::Proceso finalizado:::::")
