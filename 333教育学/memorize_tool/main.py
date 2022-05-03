import sys
from PyQt5.QtWidgets import *
import GUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = GUI.MainWindow()
    # mainWindow.show()
    sys.exit(app.exec_())