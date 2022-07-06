import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import date

neu = 'https://www.goflink.com/de-DE/shop/category/de-neu/'
frischundfertig = 'https://www.goflink.com/de-DE/shop/category/frisch-fertig/'
fleischundfisch = 'https://www.goflink.com/de-DE/shop/category/fleisch-fisch/'
grillen = 'https://www.goflink.com/de-DE/shop/category/grillen/'
backwaren = 'https://www.goflink.com/de-DE/shop/category/backwaren/'
eierundmilch = 'https://www.goflink.com/de-DE/shop/category/eier-milch/'
joghurtunddesserts = 'https://www.goflink.com/de-DE/shop/category/joghurt-desserts/'
kaese = 'https://www.goflink.com/de-DE/shop/category/kaese/'
wurstundaufschnitt = 'https://www.goflink.com/de-DE/shop/category/wurst-aufschnitt/'
alkoholfreiegetraenke = 'https://www.goflink.com/de-DE/shop/category/alkoholfreie-getraenke/'
bier = 'https://www.goflink.com/de-DE/shop/category/bier/'
weinundsekt = 'https://www.goflink.com/de-DE/shop/category/wein-sekt/'
spirituosen = 'https://www.goflink.com/de-DE/shop/category/spirituosen/'
sweetsnacks = 'https://www.goflink.com/de-DE/shop/category/suesse-snacks/'
salzigesnacks = 'https://www.goflink.com/de-DE/shop/category/salzige-snacks/'
tiefkuehl = 'https://www.goflink.com/de-DE/shop/category/tiefkuehl/'
eis = 'https://www.goflink.com/de-DE/shop/category/eis/'
veggieundvegan = 'https://www.goflink.com/de-DE/shop/category/veggie/'
konservenundfertiggerichte = 'https://www.goflink.com/de-DE/shop/category/konserven-und-fertiggerichte/'
saucenoeleundgewuerze = 'https://www.goflink.com/de-DE/shop/category/saucen-oele-gewuerze/'
aufstrichundcerealien = 'https://www.goflink.com/de-DE/shop/category/aufstrich-cerealien/'
nudelnreisgetreide = 'https://www.goflink.com/de-DE/shop/category/nudeln-reis-getreide/'
kaffeteekakao = 'https://www.goflink.com/de-DE/shop/category/kaffee-tee-kakao/'
backenunddesserts = 'https://www.goflink.com/de-DE/shop/category/backen-dessert/'
internationalekueche = 'https://www.goflink.com/de-DE/shop/category/internationale-kueche/'

drogerieundhygiene = 'https://www.goflink.com/de-DE/shop/category/drogerie-hygiene/'
kosmetik = 'https://www.goflink.com/de-DE/shop/category/kosmetik/'
haushaltundtechnik = 'https://www.goflink.com/de-DE/shop/category/kueche-haushalt-technik/'
baby = 'https://www.goflink.com/de-DE/shop/category/baby-titel/'
tierfutter = 'https://www.goflink.com/de-DE/shop/category/tierfutter/'
fitness = 'https://www.goflink.com/de-DE/shop/category/fitness/'

allproducts = []

def get_page(url):
    response = requests.get(url)
    if not response.ok:
        print("\nWebsite not found: " + response.status_code)
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        print("\nloading data from = \n" + url)
    return soup


def parse(soup):
    productslist = []
    results = soup.find_all('div', {'class': 'product-card-grid-item'})
    for item in results:
        # why? 1 div tag enthält 2 span tags (in diesen steht der preis, einer davon normalpreis der andere angebotspreis)
        result_pricediv = str(
            item.find('div', class_='price-tag --discounted'))
        result_pricediv2 = str(item.find('div', class_='price-tag'))

        splited_price1 = result_pricediv.split(" ")
        splited_price2 = result_pricediv2.split(" ")

        result_namediv = str(
            item.find('h3', {'class': 'title line-clamp-2'}).text.strip())
        splited_name = result_namediv.split(" ")
        productname = str(
            item.find('h3', {'class': 'title line-clamp-2'}).text.strip())
        replaced_name = productname.replace(",", ".")

        # wahrscheinlich wird die mengenangabe ein problem machen (vielleicht nochmal replacen oder menge in extra spalte speichern?)
        size = splited_name[len(splited_name) -
                                1].replace("(", "").replace(")", "")

        # logik = falls das produkt nicht im angebot ist, wird der alte preis auf 0 gesetzt und produkt erhält nur neuen preis
        if (len(splited_price1) < 20):
            new_price = splited_price2[8].replace(
                "€", "").replace("\xa0", "").replace("\n", "")
            old_price = 0
        else:
            new_price = splited_price2[9].replace(
                "€", "").replace("\xa0", "").replace("\n", "")
            old_price = splited_price2[17].replace(
                "€", "").replace("\xa0", "").replace("\n", "")

        # finales speichern (tabellenlogik)
        product = {
            'productname': replaced_name,
            'size': size,
            'newprice': new_price,
            'oldprice': old_price,
            'link': "https://www.goflink.com/" + item.find('a', {'class': 'focus:after:outline-ring'})['href'],
            }
        productslist.append(product)
        allproducts.append(product)
    return productslist


def output(productlist, file_name):
    current = os.getcwd()
    if not os.path.exists("database"):
        os.makedirs("database")
        os.chdir("database")
        productdf = pd.DataFrame(productlist)
        productdf.to_csv(file_name + '.csv', index=False, sep=',')
        print("Saved to CSV (" + file_name +".csv)")
        os.chdir(str(current))
    else:
        os.chdir("database")
        productdf = pd.DataFrame(productlist)
        productdf.to_csv(file_name + '.csv', index=False, sep=',')
        print("Saved to CSV (" + file_name +".csv)")
        os.chdir(str(current))
    return


today = date.today()

os.system('python3 obst.py')
output(parse(get_page(neu)), "neu")
output(parse(get_page(frischundfertig)), "frischundfertig")
output(parse(get_page(fleischundfisch)), "fleischundfisch")
output(parse(get_page(grillen)), "grillen")
output(parse(get_page(backwaren)), "backwaren")
output(parse(get_page(eierundmilch)), "eierundmilch")
output(parse(get_page(joghurtunddesserts)), "joghurtunddesserts")
output(parse(get_page(kaese)), "kaese")
output(parse(get_page(wurstundaufschnitt)), "wurstundaufschnitt")
output(parse(get_page(alkoholfreiegetraenke)), "alkoholfreiegetraenke")
output(parse(get_page(bier)), "bier")
output(parse(get_page(weinundsekt)), "weinundsekt")
output(parse(get_page(spirituosen)), "spirituosen")
output(parse(get_page(sweetsnacks)), "sweetsnacks")
print("\n\n\n\n\n\n\n\n50% finshed!\n\n\n\n\n\n\n\n")
output(parse(get_page(salzigesnacks)), "salzigesnacks")
output(parse(get_page(tiefkuehl)), "tiefkuehl")
output(parse(get_page(eis)), "eis")
output(parse(get_page(veggieundvegan)), "veggieundvegan")
output(parse(get_page(konservenundfertiggerichte)), "konservenundfertiggerichte")
output(parse(get_page(saucenoeleundgewuerze)), "saucenoeleundgewuerze")
output(parse(get_page(aufstrichundcerealien)), "aufstrichundcerealien")
output(parse(get_page(nudelnreisgetreide)), "nudelnreisgetreide")
output(parse(get_page(kaffeteekakao)), "kaffeeteekakao")
output(parse(get_page(backenunddesserts)), "backenunddesserts")
output(parse(get_page(internationalekueche)), "internationalekueche")

output(parse(get_page(drogerieundhygiene)), "drogerieundhygiene")
output(parse(get_page(kosmetik)), "kosmetik")
output(parse(get_page(haushaltundtechnik)), "haushaltundtechnik")
output(parse(get_page(baby)), "baby")
output(parse(get_page(tierfutter)), "tierfutter")
output(parse(get_page(fitness)), "fitness")


print("\n\n\n\n\nData succsessfully scraped!")
if os.path.isfile('allproducts.csv'):
    os.remove("allproducts.csv")
    os.system('python3 merge.py')

print("finshed!")