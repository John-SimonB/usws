import os
import pandas as pd
import numpy as np
import time

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


def read_recipe():
    owd = os.getcwd()
    if os.path.exists("scraper/"):
        os.chdir("scraper/")
        if os.path.isfile("Rezepte.xlsx"):
            data = pd.read_excel("Rezepte.xlsx")
            print(data)
            os.chdir(owd)
            return data
        else: print("No file found")
    else: print("Path not found")


print(open_file("Bier", "20.06"))
print(read_recipe())

