nilai=[{"NIM":"A01", "Nama": "Agustina", "Mid": 50, "UAS":80},
       {"NIM":"A02", "Nama": "Budi", "Mid": 40, "UAS":90},
       {"NIM":"A03", "Nama": "Chicha", "Mid": 100, "UAS":50},
       {"NIM":"A04", "Nama": "Donna", "Mid": 20, "UAS":100},
       {"NIM":"A05", "Nama": "Fatimah", "Mid": 70, "UAS":100}]

print("="*50)
print("NIM".ljust(10), "NAMA".ljust(10), "N.MID".rjust(10), "N.UAS".rjust(10))
print("-"*50)
for i in range(len(nilai)):
    nim  = nilai[i].get("NIM")
    nama = nilai[i].get("Nama")
    mid  = str(nilai[i].get("Mid"))
    uas  = str(nilai[i].get("UAS"))
    print(nim.ljust(10), nama.ljust(10), mid.rjust(10), uas.rjust(10))