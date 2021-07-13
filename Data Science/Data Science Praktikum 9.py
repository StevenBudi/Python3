import mysql.connector as sql
import pandas as pd

db = sql.connect(host = "127.0.0.1", port = 3306, user = "root", password = "budi", database = "world")
data = pd.read_sql("SELECT * FROM city", con=db)
data1 = pd.read_sql("SELECT *FROM country", con=db)

setBenua = set(data1["Continent"])
listBenua = {}
for benua in setBenua :
    listBenua[benua] = [["", 0],["", 0],["", 0]]

#Kode Negara dari Nama Kota
listID = {}
for i in range(len(data["Name"])):
    listID[data["Name"][i]] = data["CountryCode"][i]

#Nama Negara dari Kode Negara
listKode = {}
for i in range(len(data1["Name"])):
    listKode[data1["Code"][i]] = data1["Name"][i]

#Nama Benua dari Nama Negara
listContinent = {}
for i in range(len(data1["Name"])):
    listContinent[data1["Name"][i]] = data1["Continent"][i]

check = []
for i in range(3):
    for index, row in data.iterrows():
        kota = row["Name"]
        populasi = row["Population"]
        kode = listID.get(kota)
        negara = listKode.get(kode)
        benua = listContinent.get(negara)
        if populasi > listBenua[benua][i][1] and kota not in check:
            check.append(kota)
            listBenua[benua][i] = [kota, populasi]

for continent in listBenua :
    print(continent, end="\n")
    for city in listBenua[continent]:
        if city[1] != 0 :
            print(city[0], ":", city[1], end=";")
    print("\n")








