import os
import pandas as pd
import numpy as np
import json

# öffnet data und gibt sie als liste zurück
# bsp: open_file("angebote", "20.06")
def open_file(name, datum):
    owd = os.getcwd()
    if os.path.exists("scraper/" + datum):
        os.chdir("scraper/" + datum)
        if os.path.isfile(name + '.csv'):
            print("File found!")
            data = []
            for chunk in pd.read_csv(name + ".csv", chunksize=10, error_bad_lines=False):
                data.append(chunk)
                os.chdir(owd)
            return data
        else: print("Directory not found")
    else: print("No file found")

# productsuche in gescrapten daten erst den dateinamen, danach datum, zuletzt was gesucht wird
# bsp: search_for_product("angebote", "20.06", "Milch")
def search_for_product(file, date, search):
    print("You search for: " + search)
    if os.path.exists("scraper/" + date):
        os.chdir("scraper/" + date   )
        data = pd.read_csv(file +".csv")
        print(type(data))
        data.columns = ["productname", "size", "newprice", "oldprice", "link"]
        prodcutsearch = data.loc[data['productname'].str.contains(search)]
        if len(prodcutsearch) == 0:
            print("No product found!")
        else: print (prodcutsearch)



# beispiel für ein rezept, falls der aufbau nicht umsetzbar ist 
# bereits erkannten problem: irgendwie wird nur das zweite rezept ausgegeben (kuchen), das nudelrezept scheint
# nicht zu existieren
data = {
    "name" : "Nudeln",
    "beschreibung" : {
        "zubereitung" : "erst das wasser kochen, dann...",
        "nährwerte" : "100 kcal, 10 g fett.....",
        "menge" : 1,
        "zutaten" : {
            "1" : "Wasser",
            "2" : "Tomaten",
        },
    },
    "name" : "Kuchen",
    "beschreibung" : {
        "zubereitung" : "erst den teig kneten",
        "nährwerte" : "1000 kcal, 10 g fett.....",
        "menge" : 1,
        "zutaten" : {
            "1" : "Mehl",
            "2" : "Salz",
            "3" : "Zucker"
        },
    },
}
print(data)
#test = data.get('beschreibung').get('zutaten', 'Not Found')










# funktion funktioniert aktuell nicht
# def read_recipe():
#     owd = os.getcwd()
#     if os.path.exists("scraper/"):
#         os.chdir("scraper/")
#         if os.path.isfile("Rezepte-2.xlsx"):
#             data = pd.read_excel("Rezepte-2.xlsx")
#             os.chdir(owd)
#             return data
#         else: print("No file found")
#     else: print("Path not found")


# allgemeine notizen:
# # rezepte mit suche verbinden 
# 100g preis ausrechnen (scrape) nicht pflicht
# namesplitting anschauen (wegen menge) nicht pflicht
#Tokenizer 
#nltk