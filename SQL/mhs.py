import pymysql as pm


def OpenConnection():
    global db
    global cursor
    try :
        db = pm.connect(host = "localhost", port = 3306, user = "root", passwd= "budi", database= "db_budi")
        cursor = db.cursor()
    except :
        print("Connection Failed")

def AddData():
    while True:
        try :
            nim      = str(input("Masukkan nim                        : "))
            nama     = str(input("Masukkan nama                       : "))
            alamat   = str(input("Masukkan alamat                     : "))
            tgllahir = str(input("Masukkan Tanggal Lahir (YYYY-MM-DD) : "))
            value = (nim, nama, alamat, tgllahir)
            sql = "INSERT INTO mhs VALUES (%s, %s, %s, %s)"
            cursor.execute(sql,value)
            db.commit()
        except:
            print("Error Occured")
            db.rollback()
        add = str(input("Tambah data lagi (y/n) ? : "))
        if add.lower() == "n":
            break

def CloseConnection():
    db.close()

def SearchAll():
    sql = "SELECT * FROM mhs ORDER BY nim DESC"
    try :
        cursor.execute(sql)
        data = cursor.fetchall()
        for val in data:
            print(val[0].ljust(0), val[1].ljust(30), val[2].ljust(15), val[3].strftime("%Y-%m-%d").ljust(20))
        print("-"*70)
        print("Jumlah Mahasiswa : ", cursor.rowcount)
        db.commit()
    except :
        print("Error Occured")
        db.rollback() 

def MainMenu():
    OpenConnection()
    while True:
        print("Menu")
        print("1. Tambah Data")
        print("2. Tampil Data")
        print("3. Edit Data")
        print("4. Keluar")
        opsi = int(input("Masukkan Pilihan  : "))
        if opsi == 1:
            AddData()
        elif opsi == 2:
            SearchAll()
        elif opsi == 3:
            EditData()
        elif opsi == 4:
            break
    CloseConnection()

def EditData():
    
    while True:
        nim = str(input("Masukkan NIM   : ")).upper()
        print("1. Update Nama")
        print("2. Update Alamat")
        print("3. Update Tanggal Lahir (YYYY-MM-DD)")
        opsi = int(input("Menu Pilihan  : "))
        if opsi == 1:
            nama = str(input("Masukkan Nama Baru    : "))
            sql = "UPDATE mhs SET nama = %s WHERE nim = %s"
            value = (nama, nim)
        elif opsi == 2 :
            alamat = str(input("Masukkan Alamat Baru    : "))
            sql = "UPDATE mhs SET alamat = %s WHERE nim = %s"
            value = (alamat, nim)
        elif opsi == 3 :
            tgllahir = str(input("Masukkan Tanggal Lahir    : "))
            sql = "UPDATE mhs SET tgllahir = %s WHERE nim = %s"
            value = (tgllahir, nim)
        else :
            break
        try :
            cursor.execute(sql, value)
            db.commit()
        except :
            print("Error in editing data")
            db.rollback()
            break
        fetch = "SELECT * FROM mhs WHERE nim = %s"
        try :
            cursor.execute(fetch,nim)
            data = cursor.fetchone()
            print("NIM              : ", data[0])
            print("Nama             : ", data[1])
            print("Alamat           : ", data[2])
            print("Tanggal Lahir    : ", data[3])
            db.commit()
        except :
            print("Error in fetching data")
            db.rollback()
            break
        again = str(input("Edit data lagi (y/n)? : ")).lower()
        if again == 'n':
            break


MainMenu()
        