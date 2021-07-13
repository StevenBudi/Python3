import mysql.connector as sql
import pandas as pd 
from operator import itemgetter


db = sql.connect(host = "127.0.0.1", port = 3306, user = "root", password = "budi", database = "world")
data = pd.read_sql("SELECT * FROM city", con=db)

listPopulasi = {}
for index, row in data.iterrows():
    distrik = row["District"]
    populasi = row["Population"]
    kode = row["CountryCode"]
    if kode == "IDN":
        listPopulasi[distrik] = populasi

sorted_data = sorted(listPopulasi.items(), key = itemgetter(1), reverse=False)

for data in sorted_data:
    print(data)