import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


obstundgemuese = 'https://www.goflink.com/de-DE/shop/category/obst-gemuese/'

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
        #why? 1 div tag enthält 2 span tags (in diesen steht der preis, einer davon normalpreis der andere angebotspreis)
        result_pricediv = str(item.find('div', class_='price-tag --discounted'))
        result_pricediv2 = str(item.find('div', class_='price-tag'))
        
        splited_price1= result_pricediv.split(" ") 
        splited_price2 = result_pricediv2.split(" ") 
        
        result_namediv = str(item.find('h3', {'class': 'title line-clamp-2'}).text.strip())    
        splited_name = result_namediv.split(" ")
        productname = str(item.find('h3', {'class': 'title line-clamp-2'}).text.strip())
        replaced_name = productname.replace(",", ".")
        
        #wahrscheinlich wird die mengenangabe ein problem machen (vielleicht nochmal replacen oder menge in extra spalte speichern?)
        size = splited_name[len(splited_name) -3].replace("(", "").replace(")", "").replace(",", ".") +"S"
        if(len(size) > 4):
            size = splited_name[len(splited_name) -2].replace("(", "").replace(")", "").replace(",", ".")
        
        # logik = falls das produkt nicht im angebot ist, wird der alte preis auf 0 gesetzt und produkt erhält nur neuen preis
        if (len(splited_price1) < 20):
            new_price = splited_price2[8].replace("€", "").replace("\xa0", "").replace("\n","")
            old_price = 0
        else:
            new_price = splited_price2[9].replace("€", "").replace("\xa0", "").replace("\n","")
            old_price = splited_price2[17].replace("€", "").replace("\xa0", "").replace("\n","")

        #finales speichern (tabellenlogik)
        product = {
            'productname': replaced_name,
            'size': size,
            'newprice': new_price,
            'oldprice': old_price,
            'link': "https://www.goflink.com/" + item.find('a', {'class': 'focus:after:outline-ring'})['href'],
            }
        productslist.append(product)
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


output(parse(get_page(obstundgemuese)), "obstundgemuese")
print("\n\n\n\n\nData succsessfully scraped!")