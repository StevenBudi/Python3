import pandas as pd
from pandas import ExcelFile
from datetime import*
from operator import itemgetter

fileName = "Sample - Superstore.xls"
db = pd.read_excel(fileName, sheet_name = "Orders")
dataDate = db["Order Date"]
dataProduk = db["Product Name"]

#Setting Dictionary
Produk = set(dataProduk)

Produk_Dict = {}
for data in Produk:
    Produk_Dict[data] = 0

#Order During 2014 - 2017
for i in range(len(dataDate)):
    data = dataDate[i]
    timestamp = pd.Timestamp(data)
    date_time = timestamp.to_pydatetime()
    sdate = datetime(2014, 1, 1)
    diff = date_time - sdate
    diff = diff.days
    if diff >= 0 and diff <= 1460:
        Produk_Dict[dataProduk[i]] += 1

#Sorting Base on Value
sorted_data = sorted(Produk_Dict.items(), key = itemgetter(1), reverse = True)

for j in range(5):
    print(sorted_data[j])
