from datetime import *
def diffDate(x):
    x = x.split("-")
    tanggal = date(int(x[0]), int(x[1]), int(x[2]))
    now = datetime.date(datetime.now())
    hasil = now - tanggal
    hasil = hasil.days
    print(hasil, "hari")
    print(type(hasil))
    
diffDate("2019-08-21",)

    
