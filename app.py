import requests
from constants import URL
from bs4 import BeautifulSoup
import time

print(":::::Iniciando proceso:::::")

response = requests.get(URL)
allCompanies = []

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
        allCompanies.append(dict(name=name, url=url))
    else:
      a = el.find('a')
      url = a.get('href')
      allCompanies.append(dict(name=name, url=url))
else:
  ## error
  print("Error:", response.status_code)

data = dict(version=int(time.time()), companies=allCompanies)
print("data", data)

print(":::::Proceso finalizado:::::")
