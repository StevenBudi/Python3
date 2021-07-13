nilai = []
nim   = []
nama  = []
nilaiMhs = [{'NIM' : 'A01', 'Nama' : "Amir", 'Mid' : 50, "UAS" : 80},
           {'NIM' : 'A02', 'Nama' : "Budi", 'Mid' : 40, "UAS" : 90},
           {'NIM' : 'A03', 'Nama' : "Cici", 'Mid' : 50, "UAS" : 50},
           {'NIM' : 'A04', 'Nama' : "Dedi", 'Mid' : 20, "UAS" : 30},
           {'NIM' : 'A05', 'Nama' : "Fifi", 'Mid' : 70, "UAS" : 40}]

for i in range(len(nilaiMhs)):
    Akhir = int((nilaiMhs[i]["Mid"] + 2*nilaiMhs[i]["UAS"])/3)
    nilai.append(Akhir)

print(nilai)

for i in range(len(nilaiMhs)):
    nim.append(str(nilaiMhs[i]["NIM"]))

for i in range(len(nilaiMhs)):
    nama.append(str(nilaiMhs[i]["Nama"]))

print("Mahasiswa dengan nilai akhir tertinggi adalah ", nim[nilai.index(max(nilai))], nama[nilai.index(max(nilai))], "dengan nilai", max(nilai))





    
 


