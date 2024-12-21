class ExcelReader():


    @staticmethod
    def resdExcelFile():
        print("Reading from Excel")

class MysqlDBcon():

    @staticmethod
    def readMYSQL():
        print( "reading from MYsql")

class Tc1:
    def runTC(self):
        ExcelReader().resdExcelFile()
        MysqlDBcon.readMYSQL()

tc1= Tc1()
tc1.runTC()