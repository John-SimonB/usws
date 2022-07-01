import pandas as pd
import os
import numpy as np


listDir = os.listdir('C:/Users/serge/OneDrive/Dokumente/fiverr/Rezepte/csvs')

allproductsProductname = np.array([])
allproductsSize = np.array([])
allproductsNewprice = np.array([])
allproductsOldprice = np.array([])
allproductsLink = np.array([])

for dir in listDir:
    # productname,size,newprice,oldprice,link
    file = np.transpose(np.array(pd.read_csv(f"C:/Users/serge/OneDrive/Dokumente/fiverr/Rezepte/csvs/{dir}")))
    fileProductname = file[0]
    fileSize = file[1]
    fileNewprice = file[2]
    fileOldprice = file[3]
    fileLink = file[4]
    
    
    allproductsProductname = np.concatenate((fileProductname, allproductsProductname))
    allproductsSize = np.concatenate((fileSize, allproductsSize))
    allproductsNewprice = np.concatenate((fileNewprice, allproductsNewprice))
    allproductsOldprice = np.concatenate((fileOldprice, allproductsOldprice))
    allproductsLink = np.concatenate((fileLink, allproductsLink))

    

array = {
    "productname": allproductsProductname,
    "size": allproductsSize,
    "newprice": allproductsNewprice, 
    "oldprice": allproductsOldprice, 
    "link": allproductsLink}



columns = ['productname', 'size', 'newprice', 'oldprice', 'link']
df = pd.DataFrame(array)
df.to_csv('allproducts.csv', index=False)
