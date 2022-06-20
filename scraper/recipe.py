import os
import pandas as pd
import numpy as np

def open_file(name, datum):
    owd = os.getcwd()
    if os.path.exists("scraper/" + datum):
        os.chdir("scraper/" + datum)
        if os.path.isfile(name + '.csv'):
            print("File found!")
            data = []
            for chunk in pd.read_csv(name + ".csv", chunksize=100, error_bad_lines=False):
                data.append(chunk)
                os.chdir(owd)
            return data
        else: print("Directory not found")
    else: print("No file found")


def read_recipe():
    owd = os.getcwd()
    if os.path.exists("scraper/"):
        os.chdir("scraper/")
        if os.path.isfile("Rezepte-2.xlsx"):
            data = pd.read_excel("Rezepte-2.xlsx")
            os.chdir(owd)
            print(data)
            return data
        else: print("No file found")
    else: print("Path not found")

#open_file("eis", "20.06")

#read_recipe()

def search_for_product(file, date, search):
    print("You search for: " + search)
    if os.path.exists("scraper/" + date):
        os.chdir("scraper/" + date)
        data = pd.read_csv(file +".csv")
        print(type(data))
        data.columns = ["productname", "size", "newprice", "oldprice", "link"]
        prodcutsearch = data.loc[data['productname'].str.contains(search)]
        if len(prodcutsearch) == 0:
            print("No product found!")
        else: print (prodcutsearch)


search_for_product("bier", "20.06", "Corona")

# rezepte mit suche verbinden 


# 100g preis ausrechnen (scrape) nicht pflicht
# namesplitting anschauen (wegen menge) nicht pflicht