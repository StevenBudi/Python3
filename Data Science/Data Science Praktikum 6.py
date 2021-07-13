import pandas as pd
from pandas import ExcelFile
from datetime import*
from operator import itemgetter

fileName = "Sample - Superstore.xls"
db = pd.read_excel(fileName, sheet_name = "Orders")
dataKategori = db["Category"]
dataDate = db["Order Date"]
dataDiskon = db["Discount"]

#Setting Dict
Kategori = set(dataKategori)

Kategori_dict = {}
for data in Kategori:
    Kategori_dict[data] = 0


for i in range(len(dataDate)):
    timestamp = pd.Timestamp(dataDate[i])
    date_time = timestamp.to_pydatetime()
    sdate = datetime(2014, 1, 1)
    diff = date_time - sdate
    diff = diff.days
    if diff >= 0 and diff <= 1460:
        if dataDiskon[i] != 0:
            Kategori_dict[dataKategori[i]] += 1
    
sorted_data = sorted(Kategori_dict.items(), key = itemgetter(1), reverse = True)

for j in sorted_data:
    print(j)

dataOrder = []
for order in db["Order ID"]:
    dataOrder.append(order[:2])
setOrder = set(dataOrder)
print(setOrder)
orderDict = {}

for x in setOrder:
    orderDict[x] = 0

for y in db["Order ID"]:
    for z in setOrder:
        if y[:2] == z:
            orderDict[z] += 1

print(orderDict)

