import mysql.connector as sql
import pandas as pd
from operator import itemgetter


db = sql.connect(host = '127.0.0.1', port = 3306, user = 'root', password = "budi", database = 'world')
data = pd.read_sql("SELECT * FROM country", con=db)
dataPopulation = data["Population"]//data["SurfaceArea"]


Country_dict = {}
for j in data["Name"]:
    Country_dict[j] = 0

i = 0
for k in data["Name"]:
    index = i
    Country_dict[k] += dataPopulation[index]
    i += 1


sorted_data = sorted(Country_dict.items(), key = itemgetter(1), reverse=True)

for i in range(5):
    print(list(sorted_data[i]))

