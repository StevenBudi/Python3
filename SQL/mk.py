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
            kodemk = str(input("Masukkan Kode Mata Kuliah   : "))
            namamk = str(input("Masukkan Nama Mata Kuliah   : "))
            sks    = int(input("Masukkan Jumlah SKS         : "))
            smt    = int(input("Masukkan Semester           : "))
            sql = "INSERT INTO mk VALUES (%s, %s, %s, %s)"
            value = (kodemk, namamk, sks, smt)
            cursor.execute(sql, value)
            db.commit()
        except :
            print("Error in adding data")
            db.rollback()
        opsi = str(input("Tambah data lagi (y/n) ? : ")).lower()
        if opsi == "n":
            break

def SearchAll():
    sql = "SELECT * FROM mk ORDER BY kodemk DESC"
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        for val in data:
            print(val[0].ljust(0), val[1].ljust(30), str(val[2]).ljust(5), str(val[3]).ljust(10))
        print("-"*70)
        print("Jumlah Mata Kuliah : ", cursor.rowcount)
        db.commit()
    except :
        print("Error in fetching data")
        db.rollback

def EditData():
    while True:
        kodemk = str(input("Masukkan Kode Mata Kuliah    : "))
        print("1. Update Nama Mata Kuliah")
        print("2. Update SKS")
        print("3. Update Semester")
        opsi = str(input("Menu Pilihan  : "))
        if opsi == "1":
            namamk = str(input("Masukkan Nama Mata Kuliah   : "))
            sql = "UPDATE mk SET namamk = %s WHERE kodemk = %s"
            value = (namamk, kodemk)

        elif opsi == "2":
            sks = int(input("Masukkan Jumlah SKS    : "))
            sql = "UPDATE mk SET sks = %s WHERE kodemk = %s"
            value = (sks, kodemk)
        
        elif opsi == "3":
            smt = int(input("Masukkan Semester  : "))
            sql = "UPDATE mk SET smt = %s WHERE kodemk = %s"
            value = (smt, kodemk)

        else :
            break

        try :
            cursor.execute(sql, value)
            db.commit()
        except:
            print("Error in editing data")
            db.rollback()
        fetch = "SELECT * FROM mk WHERE kodemk = %s"
        try :
            cursor.execute(fetch, kodemk)
            data = cursor.fetchone()
            print("Kode Mata Kuliah     : ", data[0])
            print("Nama Mata Kuliah     : ", data[1])
            print("Jumlah SKS           : ", data[2])
            print("Semester             : ", data[3])
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



