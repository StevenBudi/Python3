mhs = ["K001:ROSIHAN ARI:1979-09-01:SOLO",
       "K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS",
       "K003:FAZA FAUZAN:2005-01-28:KARANGANYAR"]

mhs1=[]
for i in range(len(mhs)):
    mhs1.append(mhs[i].split(":"))
from datetime import datetime
for i in range(len(mhs1)):
    nim  = mhs1[i][0]
    nama = mhs1[i][1]
    tgl  = mhs1[i][2].split("-")
    tmpt = mhs1[i][3]
    tgl1 = '/'.join(tgl[::-1])
    print(nim.ljust(10), nama.ljust(20), tgl1, tmpt.ljust(10)) 
