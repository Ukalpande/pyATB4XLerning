from abc import ABC, abstractmethod

class ExcelReader (ABC):

    @abstractmethod
    def readFromExcel(self):
        pass
class Browser(ExcelReader):

    @abstractmethod

    def startbrowser(self):
        pass

    @abstractmethod

    def stopbrowser(self):
        pass

class Tc1(Browser):
        def startbrowser(self):
            print("starting the browser")

        def stopbrowser(self):
            print("stop the browser")
        def readFromExcel(self):
            print("Read from excel is ready")


        def runTc(self):
            self.startbrowser()
            self.readFromExcel()
            self.stopbrowser()

tc= Tc1()
tc.runTc()