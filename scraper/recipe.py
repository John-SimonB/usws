import os
import pandas as pd

def open_file(name, datum):
    
    if os.path.exists("scraper/" + datum):
        os.chdir("scraper/" + datum)
        print("Directory changed")
    else:
        print("Directory not found")
    if os.path.isfile(name + '.csv'):
        print("Datei gefunden!")

        for chunk in pd.read_csv(name + ".csv", chunksize=5):
            print(chunk)
    else:
        print("keine Datei vorhanden")

open_file("angebote", "09.06")


