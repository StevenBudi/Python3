import os
class DirectoryUtilities:
    def __init__ (self, path):
        self.value = path.upper()

    def dirList(self, dir):
        self.dir = dir
        cetak = os.listdir(self.value.lower() + ":" + "/" + self.dir)
        print(cetak)

    def makeDir(self, new):
        self.new = new
        os.mkdir(self.value.lower() + ":" + "/"+ self.new)

    def renDir(self, lama, baru):
        self.lama = lama
        self.baru = baru
        os.rename(self.value.lower() + ":" + "/"+ self.lama , self.value.lower() + ":" + "/"+ self.baru)

    def remDir(self, hapus):
        self.hapus = hapus
        os.rmdir(self.value.lower() + ":" + "/"+ self.hapus)


