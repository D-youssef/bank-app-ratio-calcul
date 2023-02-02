# import library PyQt5
import sys
from PyQt5.uic import loadUi  # this for Qt Designer app
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from interets_bank_file import interest  # intrest function file

#class of main screen
class InteretsBankScreen(QDialog) : 
    def __init__(self):
        super(InteretsBankScreen,self).__init__()
        loadUi("interets_bank.ui",self)
        self.b_delete.clicked.connect(self.delete)  # object name of buton calculate
        self.b_calculate.clicked.connect(self.calculate)  # object name of buton calculate
    # function of buton delete    
    def delete(self):
        self.input_capital.setText("")
        self.input_pourcentage.setText("")
        self.input_duree.setText("")
        self.result_capital.setText("")

    # function of buton calcul
    def calculate(self):
        try :
            c = self.input_capital.text()
            p = self.input_pourcentage.text()
            d = self.input_duree.text()

            # verify input fields if empty
            if len(c)==0 or len(p)==0 or len(d)==0:
                self.error.setText("Please input all fields !")
            else:
                self.error.setText("")
                C = float(c)
                P = float(p)
                D = int(d)

                self.result_capital.setText(str(format(interest(C,P,D),".2f")))

        except ValueError :
            self.error.setText("Please input Numbers !")
          

# main app
app = QApplication(sys.argv) 
welcome = InteretsBankScreen()
widget = QtWidgets.QStackedWidget()    
widget.addWidget(welcome)
widget.setFixedWidth(800)
widget.setFixedHeight(500)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
    
    