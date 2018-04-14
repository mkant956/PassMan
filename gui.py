import sys
from PyQt4 import QtGui
import time
def window():
   app = QtGui.QApplication(sys.argv)
   w = QtGui.QWidget()
   b = QtGui.QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle("PyQt")
   w.show()
   time.sleep(1)
   b.setText("Hello !")

   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()