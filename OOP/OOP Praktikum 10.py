import os
class DirectoryUtilities:
    def __init__ (self, path):
        self.value = path.upper()

    def dirList(self):
        dir = str(input("Masukkan nama direktori : "))
        cetak = os.listdir(self.value.lower() + ":" + "/" + dir)
        print(cetak)

    def makeDir(self):
        new = str(input("Masukkan nama folder baru : "))
        os.mkdir(self.value.lower() + ":" + "/"+ new)

    def renDir(self):
        lama = str(input("Masukkan nama file yang ingin diganti : "))
        baru = str(input("Masukkan nama file baru : "))
        os.rename(self.value.lower() + ":" + "/"+ lama , self.value.lower() + ":" + "/"+ baru)

    def remDir(self):
        hapus = str(input("Masukkan direktori yang ingin dihapus : "))
        os.rmdir(self.value.lower() + ":" + "/"+hapus)

Data = DirectoryUtilities("D")
Data.dirList()
Data.remDir()