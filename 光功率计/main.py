import sys
import time
import pyvisa as visa
import serial
from PyQt5.Qt import *
from PyQt5 import uic

class Mywindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        rm = visa.ResourceManager()
        print(rm.list_resources())

    def init_ui(self):
        self.ui = uic.loadUi('./test.ui')
        self.load_btn = self.ui.pushButton
        self.read_btn = self.ui.pushButton_2


        self.load_btn.clicked.connect(self.load)

    def data(self,data_1,data_2,data_3):
        data_0 = 'EFEF'
        # data_1 = '0X08'
        # data_2 = '0X08'
        # data_3 = ''
        data_5 = 'FFEFFFFF'
        # data = data_0 +' '+ data_1 +' '+ data_2 +' '+ data_3 +' '+ data_5
        data = data_0 + data_1 + data_2 + data_3 + data_5
        return data

    def load(self):
        global ser
        ser = serial.Serial(port='COM5',baudrate=9600)
        # hexstr = 'EFEF' + '0002080A' +'FFEFFFFF' # 复位
        # bytes_hex = bytes.fromhex(hexstr)
        # ser.write(bytes_hex)
        # time.sleep(3)
        # hexstr = 'EFEF' + '0003010206' +'FFEFFFFF' # 读取光功率
        # bytes_hex = bytes.fromhex(hexstr)
        # ser.write(bytes_hex)
        # hexstr = 'EFEF' + '000502000D0A1E' +'FFEFFFFF' # 设置波长
        # bytes_hex = bytes.fromhex(hexstr)
        # ser.write(bytes_hex)
        hexstr = 'EFEF' + '000307000A' +'FFEFFFFF' # 虚拟按键
        bytes_hex = bytes.fromhex(hexstr)
        ser.write(bytes_hex)
        time.sleep(0.5)
        for i in range(50):
                read = ser.read()
                print(read)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mywindow()
    w.ui.show()
    app.exec()