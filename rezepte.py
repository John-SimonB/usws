import pandas as pd
import numpy as np

def preisRechnung():
    # Es ist sinnvoll eine Liste mit Dictionaries zu erstellen, da die vorherige Form doppelte keywords (z.B. 2 mal "name") beinhaltete. Deshalb die [] Klammern :)
    rezepte =[{"name": "Nudeln", "beschreibung" : {
                "zubereitung" : "erst das wasser kochen, dann...",
                "nährwerte" : "100 kcal, 10 g fett.....",
                "menge" : ["100g", "10000000g"],
                "zutaten" : ["Arla Butter Kaergarden Gesalzen 250g", "Arla Butter Kaergarden Gesalzen 250g"],
                "bild" : "https://images.pexels.com/photos/2092906/pexels-photo-2092906.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"}},

                {"name": "Kuchen", "beschreibung" : {
                "zubereitung" : "erst das wasser kochen, dann...",
                "nährwerte" : "100 kcal, 10 g fett.....",
                "menge" : ["200g"],
                "zutaten" : ["Wiltmann Geflügelsalami 80g"],
                "bild" : "https://images.pexels.com/photos/291528/pexels-photo-291528.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"}},
                
                {"name": "Bla", "beschreibung" : {
                "zubereitung" : "erst das wasser kochen, dann...",
                "nährwerte" : "100 kcal, 10 g fett.....",
                "menge" : ["200g"],
                "zutaten" : ["Wiltmann Geflügelsalami 80g"],
                "bild" : "https://images.pexels.com/photos/8862752/pexels-photo-8862752.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"}},
                {"name": "123123123", "beschreibung" : {
                "zubereitung" : "erst das wasser kochen, dann...",
                "nährwerte" : "100 kcal, 10 g fett.....",
                "menge" : ["200g"],
                "zutaten" : ["Wiltmann Geflügelsalami 80g"],
                "bild" : "https://images.pexels.com/photos/8862752/pexels-photo-8862752.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"}}
            ]


    # productname,size,newprice,oldprice,link
    angeboteArray = np.transpose(np.array(pd.read_csv('angebote.csv')))
    allproductsArray = np.transpose(np.array(pd.read_csv('allproducts.csv')))

    # Überprüfe, ob mindestens 1 Zutat sich in der angebote.csv befindet
    for i in rezepte:
        preis = 0
        zutatenCount = 0
        for j in i["beschreibung"]["zutaten"]:
            # finde mengenangabe
            

            # WENN: Suche alle Produkte für das Rezept in der CSV und berechne den Preis für das fertige Gericht.
            if j in angeboteArray[0]:
                # find size, wenn es sich um eine Liste handelt, index, keine Liste, kein Index
                if type(angeboteArray[1][np.where(angeboteArray[0] == j)]).__module__ == np.__name__:
                    sizeProd = angeboteArray[1][np.where(angeboteArray[0] == j)][0]
                else:
                    sizeProd = angeboteArray[1][np.where(angeboteArray[0] == j)]
                sizeRez = i["beschreibung"]["menge"][zutatenCount]
                
                # mögliche Einheiten sind g oder kg, l oder ml
                if sizeRez[-1] == "g" or sizeRez[-1] == "l":
                    if sizeRez[-2] == "k" or sizeRez[-2] == "m":
                        sizeRezNum = float(sizeRez[:-2])
                    else:
                        sizeRezNum = float(sizeRez[:-1])
                
                if sizeProd[-1] == "g" or sizeProd[-1] == "l":
                    if sizeProd[-2] == "k" or sizeProd[-2] == "m":
                        sizeProdNum = float(sizeProd[:-2])
                    else:
                        sizeProdNum = float(sizeProd[:-1])
                
                
                # [0], da es sich nur um ein Element handelt
                preis += float(angeboteArray[2][np.where(angeboteArray[0] == j)][0].replace(",", "."))*sizeRezNum/sizeProdNum
            # Befindet sich das gesuchte Produkt nicht in der Angebote.csv, dann suche das Produkt in der allproducts.csv für den Preis.
            else:
                # find size (hier wird sonst array an sizeProd ausgegeben, deshalb [0])
                sizeProd = allproductsArray[1][np.where(allproductsArray[0] == j)][0]
                sizeRez = i["beschreibung"]["menge"][zutatenCount]

                # mögliche Einheiten sind g oder kg, l oder ml
                if sizeRez[-1] == "g" or sizeRez[-1] == "l":
                    if sizeRez[-2] == "k" or sizeRez[-2] == "m":
                        sizeRezNum = float(sizeRez[:-2])
                    else:
                        sizeRezNum = float(sizeRez[:-1])
                
                if sizeProd[-1] == "g" or sizeProd[-1] == "l":
                    if sizeProd[-2] == "k" or sizeProd[-2] == "m":
                        sizeProdNum = float(sizeProd[:-2])
                    else:
                        sizeProdNum = float(sizeProd[:-1])
                preis += float(allproductsArray[2][np.where(allproductsArray[0] == j)][0].replace(",", "."))*sizeRezNum/sizeProdNum

            i.update({'preis': round(preis, 2)})
            zutatenCount += 1

    return rezepte