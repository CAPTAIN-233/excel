import sys
import time
from PyQt5 import uic
from PyQt5.Qt import QApplication,QWidget,QThread

class Myprocess1(QThread):
    # def __init__(self):
    #     super().__init__()
    def run(self):
        for i in range(10):
            print('process_{0}'.format(i))
            time.sleep(1)

class Myprocess2(QThread):
    def run(self):
        for i in range(10):
            print('process_{}'.format(i+10))
            time.sleep(1)

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi('./多线程.ui')
        lineedit = self.ui.textEdit
        btn_1 = self.ui.pushButton_2
        btn_2 = self.ui.pushButton

        btn_1.clicked.connect(self.click_1)
        btn_2.clicked.connect(self.click_2)

    def click_1(self):
        self.my_process = Myprocess2()
        self.my_process.start()

    def click_2(self):
        self.my_process = Myprocess1()
        self.my_process.start()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mywindow()
    w.ui.show()
    app.exec()