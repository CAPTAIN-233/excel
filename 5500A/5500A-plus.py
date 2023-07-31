import os
import sys
import serial
import time
from PyQt5 import uic
from PyQt5.QtWidgets import *

class Mywindow(QWidget):

    def __init__(self):
        super().__init__() # 继承父类
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi('./5500A.ui') # 读取ui
        # print(self.ui.__dict__) # 查看ui控件
        self.load_btn = self.ui.pushButton # 加载按钮
        self.change_btn = self.ui.pushButton_2 # 更改参数按钮
        self.textbrowser = self.ui.textBrowser # 文本显示
        self.com_choose = self.ui.comboBox # 串口选择
        self.baud_choose = self.ui.comboBox_2 # 波特率选择

        # 绑定信号与槽函数
        self.load_btn.clicked.connect(self.load) # 绑定加载信号
        self.change_btn.clicked.connect(self.change) # 绑定更改信号

    # 定义加载函数
    def load(self):
        file = open('./5500A.txt', mode='r')
        ser = serial.Serial(port=self.com_choose.currentText(), baudrate=self.baud_choose.currentText()) # 初始化 设置串口、波特率
        for f in file:
            print(f,end='')
            ser.write(f.encode('utf-8')) # 发送数据
            time.sleep(0.1)
        self.textbrowser.setText(f)
        #self.textbrowser.repaint()

    # 定义更改函数
    def change(self):
        os.system(r'notepad ./5500A.txt') # 打开txt文件窗口

# 页面加载
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mywindow()
    w.ui.setWindowTitle('5500A')
    w.ui.show()
    app.exec()



# 读取txt
# file = open('./5500A.txt',mode='r')
# for f in file:
#     print(f)
#