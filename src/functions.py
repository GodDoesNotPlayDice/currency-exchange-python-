from bs4 import BeautifulSoup
from pytz import country_names
import requests as rq
root = "https://www.xe.com/es/currencyconverter/convert/"
flags_root = "https://www.iban.com"
def flags():
    web = f"{flags_root}/currency-codes"
    get = rq.get(web)
    content = get.text
    soup = BeautifulSoup(content, "lxml")
    bigTable = soup.find("table",class_="table table-bordered downloads tablesorter")
    table = bigTable.find("tbody")
    country = table.find_all("td")
    flgs,flg = [],[]
    cont = 0
    for i in country:
        if cont == 3:
            cont = 0
            flgs.append(flg)
            flg = []
        else:
            flg.append(i.text)
            cont+=1

    print(flgs)
    #countrys = str(country).split(",")
    #for i in countrys:
    #    print(i)

flags()