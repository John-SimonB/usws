import os
import pandas as pd
import numpy as np
import time

def open_file(name, datum):
    
    if os.path.exists("scraper/" + datum):
        os.chdir("scraper/" + datum)
        print("Directory changed")
    else:
        print("Directory not found")
    if os.path.isfile(name + '.csv'):
        print("Datei gefunden!")
        data = []
        for chunk in pd.read_csv(name + ".csv", chunksize=10, error_bad_lines=False):
            data.append(chunk)
        print(data)
    else:
        print("keine Datei vorhanden")

open_file("angebote", "20.06")

