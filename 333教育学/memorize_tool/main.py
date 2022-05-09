import sys
from PyQt5.QtWidgets import *
import GUI
import JsonFunc

if __name__ == '__main__':
    JsonFunc.refresh_date()
    app = QApplication(sys.argv)
    mainWindow = GUI.MainWindow()
    # mainWindow.show()
    sys.exit(app.exec_())