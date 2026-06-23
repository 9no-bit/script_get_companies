import requests
from constants import URL
from bs4 import BeautifulSoup

print(":::::Iniciando proceso:::::")

response = requests.get(URL)

if response.status_code == 200:
  ## exito
  print("Datos obtenidos:")
  sopa = BeautifulSoup(response.text, 'html.parser')
  lista = sopa.find(class_='operators-list')
  #print(lista)
  elements = lista.find_all("li")
  for el in elements:
    name = el.get('data-name')
    els = el.select("div.accordion-body")
    if len(els) > 0:
      pass
    else:
      a = el.find('a')
      url = a.get('href')
      print(name, url)

else:
  ## error
  print("Error:", response.status_code)

print(":::::Proceso finalizado:::::")

"""
<li class="accordion-item" data-list-item-id="e57e084ee04ca84f1d2d349fb27b812b9" data-name="Dalefon">
  <p>
    <button aria-expanded="false" class="accordion-header" type="button">
      <span class="acc-name">Dalefon</span><span class="acc-badge">2</span>
      <span class="acc-arrow"></span>
    </button>
  </p>
  <div class="accordion-body">
    <a class="operator-btn" href="https://www.dalefon.mx/vinculatulinea" rel="noopener" target="_blank">Dalefon</a>
    <a class="operator-btn" href="https://www.internetbienestarmex.com/vinculatulinea" rel="noopener" target="_blank">Dalefon/Internet para el Bienestar</a>
  </div>
</li>
"""