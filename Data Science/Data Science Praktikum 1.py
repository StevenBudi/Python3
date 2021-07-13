import pandas as pd
from pandas import ExcelFile
from datetime import *

fileName = "Sample - Superstore.xls"
db = pd.read_excel(fileName, sheet_name = "Orders")
sumKanada = 0
sumDate = 0
dataOrder = db["Order ID"]
dataDate  = db["Order Date"]


i = 0
#All Order From Canada
for data in dataOrder:
    if data[:2] == "CA":
        index = i
        #All Order During November 2016
        data1 = dataDate[index]
        timeStamp = pd.Timestamp(data1)
        date_time = timeStamp.to_pydatetime()
        sdate = datetime(2016,11,30)
        difference = (sdate - date_time).days
        if difference >= 0 and difference <= 30:
            sumKanada += 1
    else :
        i += 1

print(sumKanada)




