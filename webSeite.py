from sys import path
from flask import Flask, redirect, url_for, render_template, request
import rezepte as rp
import numpy as np
import os
import datetime as dt
from pathlib import Path

def createApp(secretKey):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secretKey
    return app

app = createApp('REZEPTE')



# verschiedene Seiten
@app.route("/")
def test():
    return render_template("home.html")


#dsafs
@app.route("/Rezeptsuche", methods=["POST", "GET"])
def searchPage():
    if request.method == "POST":
        word = request.form['nm']

        f = Path('angebote.csv')
        f2 = Path('allproducts.csv')

        today = dt.datetime.now().date()       
        sales = dt.datetime.fromtimestamp(f.stat().st_mtime).date()
        allproducts = dt.datetime.fromtimestamp(f2.stat().st_mtime).date()
        # auskommentiert weil angebote jetzt nicht mehr unter dem link .../angebote erreichbar sind
        # if (today == sales):
        #     print("Datei ist aktuell")
        #     print("Heutiges Datum: " + str(today))
        #     print("Datei Datum: " + str(sales))
        #     pass
        # else:
        #     print("Datei nicht aktuell")
        #     print("Heutiges Datum: " + str(today))
        #     print("Datei Datum: " + str(sales))
        #     if os.path.isfile('angebote.csv'):
        #         os.remove("angebote.csv")
        #         os.system('python3 angebotedatascrape.py')

        #time.sleep(5)
        # ScrapeThread = threading.Thread(target = os.system('python Flink_Scrape.py'))
        #ScrapeThread.start()
        #ScrapeThread.join()
        rezepte = rp.preisRechnung()
        
        nameArray = []
        zubereitungArray = []
        naehrwerteArray = []
        zutatenArray = []
        mengeArray = []
        preisArray = []
        bildArray = []
        linkArray = []
        picArray = []
        # rezepte herausfiltern, welche dem Namen entsprechen
        for rezept in rezepte:
            if word in rezept["name"]:
                nameArray.append(rezept["name"])
                zubereitungArray.append(rezept["beschreibung"]["zubereitung"])
                naehrwerteArray.append(rezept["beschreibung"]["nährwerte"])
                bildArray.append(rezept["beschreibung"]["bild"])
                zutatenArray.append(rezept["beschreibung"]["zutaten"])
                mengeArray.append(rezept["beschreibung"]["menge"])
                linkArray.append(rezept["beschreibung"]["link"])
                picArray.append(rezept["pic"])
                preisArray.append(rezept["preis"])
                
        # rezepte nach Preis sortieren
        nameArray = [x for _, x in sorted(zip(preisArray, nameArray))]
        bildArray = [x for _, x in sorted(zip(preisArray, bildArray))]
        zubereitungArray = [x for _, x in sorted(zip(preisArray, zubereitungArray))]
        naehrwerteArray = [x for _, x in sorted(zip(preisArray, naehrwerteArray))]
        zutatenArray = [x for _, x in sorted(zip(preisArray, zutatenArray))]
        mengeArray = [x for _, x in sorted(zip(preisArray, mengeArray))]
        linkArray = [x for _, x in sorted(zip(preisArray, linkArray))]
        picArray = [x for _, x in sorted(zip(preisArray, picArray))]
        preisArray = np.sort(np.array(preisArray).astype(float))
        
        return render_template("Rezeptsuche.html", nameArray=nameArray, zubereitungArray=zubereitungArray, naehrwerteArray=naehrwerteArray, zutatenArray=zutatenArray, mengeArray=mengeArray, preisArray=preisArray, bildArray=bildArray, sales=sales,allproducts=allproducts, linkArray=linkArray,picArray=picArray,  writeBool=True)
    else:
        f = Path('angebote.csv')
        f2 = Path('allproducts.csv')
        sales = dt.datetime.fromtimestamp(f.stat().st_mtime).date()
        allproducts = dt.datetime.fromtimestamp(f2.stat().st_mtime).date()
        nameArray = []
        zubereitungArray = []
        naehrwerteArray = []
        zutatenArray = []
        mengeArray = []
        preisArray = []
        bildArray = []
        linkArray = []
        picArray = []
        return render_template("Rezeptsuche.html", nameArray=nameArray, zubereitungArray=zubereitungArray, naehrwerteArray=naehrwerteArray, zutatenArray=zutatenArray, mengeArray=mengeArray, preisArray=preisArray, bildArray=bildArray, sales=sales,allproducts=allproducts,linkArray=linkArray,picArray=picArray, writeBool = False)







if __name__ == '__main__':
    app.run(debug=True) 


