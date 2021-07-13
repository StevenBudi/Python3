import pandas as pd
from pandas import ExcelFile
from datetime import *
from operator import itemgetter

fileName = "Sample - Superstore.xls"
db = pd.read_excel(fileName, sheet_name = "Orders")
dataSegment = db["Segment"]
dataDate = db["Order Date"]

#Setting Dictionary
segment = set(dataSegment)

dict_0 = {}
for i in segment:
    dict_0[i] = 0


#Order During 2016 - 2017
for i in range(len(dataDate)):
    data1 = dataDate[i]
    timestamp = pd.Timestamp(data1)
    date_time = timestamp.to_pydatetime()
    sdate = datetime(2016, 1, 1)
    difference = date_time - sdate
    difference = difference.days
    if difference >= 0 and difference <= 730:
        dict_0[dataSegment[i]] += 1

#Sorting Segment Base On The Value Number
sorted_data = sorted(dict_0.items(),
                    key = itemgetter(1),
                    reverse = True)

print(sorted_data[0])
                    





