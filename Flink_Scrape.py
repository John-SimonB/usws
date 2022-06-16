"""
Created on Mon May 16 17:05:14 2022

@author: john-simonbachhuber
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

angebote = 'https://www.goflink.com/de-DE/shop/category/angebote/'
neu = 'https://www.goflink.com/de-DE/shop/category/de-neu/'
frischundfertig  = 'https://www.goflink.com/de-DE/shop/category/frisch-fertig/'
obstundgemuese = 'https://www.goflink.com/de-DE/shop/category/obst-gemuese/'
fleischundfisch = 'https://www.goflink.com/de-DE/shop/category/fleisch-fisch/'
grillen = 'https://www.goflink.com/de-DE/shop/category/grillen/'
backwaren = 'https://www.goflink.com/de-DE/shop/category/backwaren/'
eierundmilch ='https://www.goflink.com/de-DE/shop/category/eier-milch/'
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
fitness ='https://www.goflink.com/de-DE/shop/category/fitness/'

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
        price_div = item.find('div', class_='price-tag --discounted')
        price_div2 = item.find('div', class_='price-tag')
        
    
        results = str(price_div)
        results2 = str(price_div2)
        
        splited = results.split(" ") 
        splited2 = results2.split(" ") 
        
        if (len(splited) < 20):
            new_price = splited2[8].replace("€", "").replace("\xa0", "").replace("\n","")
            old_price = 0
        else:
            new_price = splited[9].replace("€", "").replace("\xa0", "").replace("\n","")
            old_price = splited[17].replace("€", "").replace("\xa0", "").replace("\n","")
        product = {
            'productname': item.find('h3', {'class': 'title line-clamp-2'}).text.strip(),
            'newprice': new_price,
            'oldprice': old_price,
            'link': "https://www.goflink.com/" + item.find('a', {'class': 'focus:after:outline-ring'})['href'],
            }
        productslist.append(product)
    return productslist

def output(productlist, file_name):
    productdf = pd.DataFrame(productlist)
    productdf.to_csv(file_name + '.csv', index=False, sep=';')
    print("Saved to CSV (" + file_name +".csv)")
    return

output(parse(get_page(angebote)), "angebote")
output(parse(get_page(neu)), "neu")
output(parse(get_page(frischundfertig)), "frischundfertig")
output(parse(get_page(obstundgemuese)), "obstundgemuese")
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