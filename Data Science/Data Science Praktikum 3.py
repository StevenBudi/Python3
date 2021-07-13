import pandas as pd
from pandas import ExcelFile
from datetime import *
from operator import itemgetter

fileName = "Sample - Superstore.xls"
db = pd.read_excel(fileName, sheet_name = "Orders")
dataOrder = db["Order ID"]
dataDate = db["Order Date"]
dataState = db["State"]

#Setting Dictionary
State = set(dataState)

State_dict = {}
for data in State:
    State_dict[data] = 0

i = 0
#Order From America
for data in dataOrder:
    if data[:2] == "US":
        index = i
        #Order During 2016 - 2017
        data1 = dataDate[index]
        timestamp = pd.Timestamp(data1)
        date_time = timestamp.to_pydatetime()
        sdate = datetime(2017, 1, 1)
        difference = date_time - sdate
        difference = difference.days
        if difference >= 0 and difference <= 365:
            State_dict[dataState[index]] += 1
        i += 1

#Sorting State Based on Value
sorted_data = sorted(State_dict.items(),
                    key = itemgetter(1),
                    reverse = False)

print(sorted_data)