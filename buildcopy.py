import shutil
from zipfile import ZipFile

class buildcopy:

    def __init__(self, sourcePath, destPath):
        self.sourcePath = sourcePath
        self.destPath = destPath
        #shutil.copyfile('C:/Harish/Old_T450S_Data/Builds/Jordan.1/611rts42devesigsplit.zip', 'C:/builds/611rts42devesigsplit.zip')

    def copy(self):
        try:
         shutil.copyfile(self.sourcePath, self.destPath)

        except IOError as e:
            exit("Copy failed")

    def extractZip(self, fileName):
        # Create a ZipFile Object and load sample.zip in it
        #with ZipFile(fileName, 'r') as zipObj:
        zipObj = ZipFile(fileName, 'r')
        zipObj.extractall('C:/builds')

if __name__ == "__main__":
    build = buildcopy('C:/Harish/Old_T450S_Data/Builds/Jordan.1/611rts42devesigsplit.zip', 'C:/builds/611rts42devesigsplit.zip')
    build.copy()
    build.extractZip(build.destPath)

