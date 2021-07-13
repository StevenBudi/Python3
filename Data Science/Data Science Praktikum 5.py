import pandas as pd
from pandas import ExcelFile
from datetime import*

fileName = "Sample - Superstore.xls"
db = pd.read_excel(fileName, sheet_name = "Orders")
dataDate = db["Order Date"]
dataProfit = db["Profit"]
dataOrder = db["Order ID"]
sumKanada = 0
sumAmerika = 0

i = 0
for data in dataOrder:
    index = i
    timestamp = pd.Timestamp(dataDate[i])
    date_time = timestamp.to_pydatetime()
    sdate = datetime(2016, 1, 1)
    diff = date_time - sdate
    diff = diff.days
    if diff >= 0 and diff <= 730:
        if data[:2] == "CA":
            sumKanada += dataProfit[i]
        else :
            sumAmerika += dataProfit[i]
    i += 1
        
print(sumKanada)
print(sumAmerika)

