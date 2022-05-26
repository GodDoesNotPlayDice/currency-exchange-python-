from bs4 import BeautifulSoup
import requests as rq

root = 'https://subslikescript.com' # ROOT (Raiz)
web = f'{root}/movies'
get = rq.get(web)
content = get.text
soup = BeautifulSoup(content, 'lxml')
box = soup.find('article', class_='main-article') 
links = [] 
for link in box.find_all('a', href=True): # Conseguir todos los elementos de un elemento.
    links.append(link['href'])
for link in links:
    web = f'{root}/{link}'
    get = rq.get(web)
    content = get.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article') 
    h1 = box.find('h1').get_text()
    script = box.find('div',class_= 'full-script').get_text(strip=True, separator=' ')
    try:
        with open(f'Seccion_3/scripts/{str(h1)}.txt','w') as arch:
            arch.write(str(script))
    except UnicodeEncodeError:
        with open(f'Seccion_3/scripts/{str(h1)}.txt','w', encoding='utf-8') as arch:
            arch.write(str(script))
print("Proceso terminado")
        