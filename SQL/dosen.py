import pymysql as pm

def OpenConnection():
    global db
    global cursor
    try :
        db = pm.connect(host= "localhost", port = 3306, user="root", passwd="budi", database="db_budi")
        cursor = db.cursor()
    except :
        print("Connection Failed")

def ClosedConnection():
    db.close()

def AddData():
    while True:
        try :
            nip    = str(input("Masukkan Nomer Induk Dosen        : "))
            nama   = str(input("Masukkan Nama Dosen               : "))
            status = str(input("Masukkan Status (tetap/non tetap) : ")).lower()
            prodi  = str(input("Masukkan Semester (P1/P2/P3/P4)   : ")).upper()
            sql = "INSERT INTO dosen VALUES (%s, %s, %s, %s)"
            value = (nip, nama, status, prodi)
            cursor.execute(sql, value)
            db.commit()
        except :
            print("Error in adding data")
            db.rollback()
        opsi = str(input("Tambah data lagi (y/n) ? : ")).lower()
        if opsi == "n":
            break

def SearchAll():
    sql = "SELECT * FROM dosen ORDER BY nip DESC"
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        for val in data:
            print(val[0].ljust(0), val[1].ljust(10), str(val[2]).ljust(5), str(val[3]).ljust(10))
        print("-"*70)
        print("Jumlah Dosen : ", cursor.rowcount)
        db.commit()
    except :
        print("Error in fetching data")
        db.rollback

def EditData():
    while True:
        nip = str(input("Masukkan Nomer Induk Dosen    : "))
        print("1. Update Nama Dosen")
        print("2. Update Status")
        print("3. Update Prodi")
        opsi = str(input("Menu Pilihan  : "))
        if opsi == "1":
            nama = str(input("Masukkan Nama Dosen   : "))
            sql = "UPDATE dosen SET nama = %s WHERE nip = %s"
            value = (nama, nip)

        elif opsi == "2":
            status = str(input("Masukkan Status (tetap/ non tetap)    : ")).lower()
            sql = "UPDATE dosen SET status = %s WHERE nip = %s"
            value = (status, nip)
        
        elif opsi == "3":
            prodi = str(input("Masukkan Prodi (P1/P2/P3/P4)  : ")).upper()
            sql = "UPDATE dosen SET prodi = %s WHERE nip = %s"
            value = (prodi, nip)

        else :
            break

        try :
            cursor.execute(sql, value)
            db.commit()
        except:
            print("Error in editing data")
            db.rollback()
        fetch = "SELECT * FROM dosen WHERE nip = %s"
        try :
            cursor.execute(fetch, nip)
            data = cursor.fetchone()
            print("Nomer Induk Dosen  : ", data[0])
            print("Nama Dosen         : ", data[1])
            print("Status Dosen       : ", data[2])
            print("Prodi              : ", data[3])
            db.commit()
        except :
            print("Error in fetching data")
            db.rollback()
        opsi = str(input("Update data lagi (y/n) ? : "))
        if opsi == "n":
            break

def MainMenu():
    OpenConnection()
    while True:
        print("Menu")
        print("1. Tambah Data")
        print("2. Tampil Data")
        print("3. Update Data")
        print("4. Exit")
        opsi = str(input("Menu Pilihan  : "))
        if opsi == "1":
            AddData()
        elif opsi == "2":
            SearchAll()
        elif opsi == "3":
            EditData()
        elif opsi == "4":
            break
        else :
            print("Error")
    ClosedConnection()
            
MainMenu()
