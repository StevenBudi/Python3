import mysql.connector as sql
import pandas as pd
import string

db = sql.connect(host = "127.0.0.1", port = 3306, user = "root", password = "budi", database = "world")
data  = pd.read_sql("SELECT * FROM countryLanguage", con=db)
data1 = pd.read_sql("SELECT *FROM country", con=db)

def process():
    global listNegara
    listNegara = {}
    for kode in data["CountryCode"]:
        listNegara[kode] = ['', 0]

    for __index,row in data.iterrows():  
        bahasa = row["Language"]
        kode = row["CountryCode"]
        persen = row["Percentage"]
        if persen >= listNegara[kode][1]:
            listNegara[kode] = [bahasa, persen]

    global code
    code = {}
    for i in range(len(data1["Name"])):
        code[data1["Name"][i]] =  data1["Code"][i]


def getData(x):
    process()
    x = str(x)
    x = string.capwords(x)
    Kode = code.get(x)
    Bahasa = listNegara.get(Kode)
    print(Kode ,":", Bahasa)

getData("mexico")

    


