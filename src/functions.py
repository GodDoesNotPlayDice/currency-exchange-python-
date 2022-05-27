import pandas as pd
from bs4 import BeautifulSoup
import requests as rq
import time as t
print("Cargando data...")
root = "https://www.xe.com/es/currencyconverter/convert"
flags_root = "https://www.iban.com"
def countrys():
    web = f"{flags_root}/currency-codes"
    get = rq.get(web)
    content = get.text
    soup = BeautifulSoup(content, "lxml")
    bigTable = soup.find("table",class_="table table-bordered downloads tablesorter")
    table = bigTable.find("tbody")
    country = table.find_all("td")
    countrys,aux = [],[]
    cont = 0
    for i in country:
        if cont == 3:
            cont = 0
            countrys.append(aux)
            aux= []
        else:
            aux.append(i.text)
            cont+=1
    return countrys
def currencysFormatter(countrys,value):
    arr = []
    for i in countrys:
        arr.append(str(i[value]).strip())
    arr = list(filter(('').__ne__,arr))
    return arr
def fechaCurrency(flag1,flag2):
        web = f'{root}/?Amount=10&From={flag1}&To={flag2}'
        get = rq.get(web)
        content = get.text
        soup = BeautifulSoup(content, 'lxml')
        div = soup.find('div',class_='result__LiveSubText-sc-1bsijpp-2 iKYXwX')
        date_time = div.text
        return date_time

def fecha_hoy():
    fecha = t.localtime()
    arr = []
    for i in fecha:
        arr.append(str(i))
    return arr

def currency_comparing(flag1,flag2):
    try:
        arr = []
        web = f'{root}/?Amount=10&From={flag1}&To={flag2}'
        get = rq.get(web)
        content = get.text
        soup = BeautifulSoup(content, 'lxml')
        div = soup.find('div',class_='unit-rates___StyledDiv-sc-1dk593y-0 dEqdnx')
        value = div.find('p')
        for i in value.text.split(' ')[3]:
            arr.append(i)
        value = ''.join(arr)
        value = value.replace(',','.')
        return value
    except AttributeError:
        return 'Uno de los codigos no pudo ser contrado'

def currencys(curr):
    indexs = []
    arr = []
    cont = 0
    for i in curr:
        if i[1] == 'No universal currency':
            arr.append(i)
            indexs.append(cont)
        cont+=1
    curr[8][-1] = 'XCD'
    curr[182][-1] = 'ILS'
    curr[221][-1] = 'GBP'
    return arr,curr
noUniversalCountrys,country = currencys(countrys())
def countrys_table(countrys,divisa,div_code):
    dict_all = {f"Paises" : countrys, "Divisa": divisa, "Codigo" : div_code}
    data_frame = pd.DataFrame.from_dict(dict_all)
    return data_frame
tablaDivisas = countrys_table(currencysFormatter(country,0),currencysFormatter(country,1),currencysFormatter(country,2))
tablaDivisas.to_csv('src/Divisas.csv')

# Respaldo DIVISAS (csv)

def validCountry(valid,index):
    if valid:
        nombre = currencysFormatter(country,0)[index]
        divisa = currencysFormatter(country,1)[index]
        codigo_div = currencysFormatter(country,2)[index]
        return f'Nombre: {nombre.capitalize()} | Divisa: {divisa.capitalize()} | Codigo_divisa: {codigo_div}'
    else:
        return f'(VALID COUNTRY) --Pais no encontrado!'

def historial(from_,to_,valueActual,value,date_time,time,value_time):
    try:
        return f'Pais de: {currencysFormatter(country,0)[from_]} A Pais de destino: {currencysFormatter(country,0)[to_]},\n Valor Actual: {valueActual}, Valor converitido: {value}\n Actualizacion del valor: {value_time}\n Fecha y Hora de la conversion: {date_time}, {time}'
    except IndexError:
        return 'INDEX ERROR'