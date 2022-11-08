from gui.adrgui import *


if __name__ == "__main__":
    # Init Gui
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.init_backend() # Initialize backend, this may take a few seconds
    MainWindow.show()
    sys.exit(app.exec_())