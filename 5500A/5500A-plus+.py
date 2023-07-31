import os
import sys
import datetime
import time
import serial
from PyQt5 import uic
from PyQt5.Qt import *

class Out(QThread): # 输出数据子进程


    def __init__(self):
        super().__init__()


    def run(self):
        file = open('./5500A.txt')
        #print(Mywindow.com_choose.currentText())
        ser = serial.Serial(port=com_send , baudrate=baud_send)
        ser.write('*CLS\r\n'.encode('utf-8'))
        time.sleep(0.2)
        ser.write(('*SRE 8\r\n').encode('utf-8'))
        time.sleep(0.2)
        ser.write('LIMIT33MA,-33MA\r\n'.encode('utf-8'))
        time.sleep(0.2)
        for f in file:
            ser.write('OUT{0}\r\n'.format(f).encode('utf-8'))
            time.sleep(0.2)
        ser.write('STOP\r\n'.encode('utf-8'))

class In(QThread): # 读入数据子进程
    def __init__(self):
        super().__init__()

    def run(self):
        ser = serial.Serial(port=com_come , baudrate=baud_come)
        while True:
            com_input = ser.read()
            if com_input:
                income = com_input.decode('utf-8')
                with open('./output.txt','a+') as output:
                    output.write('{0} 收到输入为  {1}\n'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),income))
                print(income)

class Ini(QThread): # 打开参数文件夹子进程
    def __init__(self):
        super().__init__()

    def run(self):
        os.system(r'notepad ./5500A.txt') # 打开txt文件窗口

class Open(QThread): # 打开读入数据文件夹子进程
    def __init__(self):
        super().__init__()

    def run(self):
        os.system(r'notepad ./output.txt')

class Mywindow(QWidget):

    def __init__(self):
        super().__init__() # 继承父类
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi('./5500A.ui') # 读取ui
        # print(self.ui.__dict__) # 查看ui控件
        self.load_btn = self.ui.pushButton # 加载按钮
        self.change_btn = self.ui.pushButton_2 # 更改参数按钮
        self.read_btn = self.ui.pushButton_3 # 读入按钮
        self.open_btn = self.ui.pushButton_4 # 打开读入文件夹
        self.brush_output_btn = self.ui.pushButton_6 # 查看/刷新输入
        self.brush_input_btn = self.ui.pushButton_5 # 查看、刷新输出
        self.textbrowser = self.ui.textBrowser # 文本显示
        self.send_com_choose = self.ui.comboBox # 发送串口选择
        self.come_com_choose = self.ui.comboBox_3 # 接收串口选择
        self.baud_choose = self.ui.comboBox_2 # 波特率选择
        # 绑定信号与槽函数
        self.load_btn.clicked.connect(self.load) # 绑定加载信号
        self.change_btn.clicked.connect(self.change) # 绑定更改信号
        self.read_btn.clicked.connect(self.read) # 绑定读入信号
        self.open_btn.clicked.connect(self.open) # 绑定打开信号
        self.brush_output_btn.clicked.connect(self.Brush_output)  # 绑定输出刷新信号
        self.brush_input_btn.clicked.connect(self.Brush_input) # 绑定输入刷新信号



    # 定义加载函数
    def load(self):
        global com_send,baud_send
        com_send = self.send_com_choose.currentText() # 为输出端口选择赋值
        baud_send = self.baud_choose.currentText() # 为波特率选择赋值
        self.thread_1 = Out()
        self.thread_1.start()

    def read(self):
        global com_come,baud_come,income
        com_come = self.come_com_choose.currentText() # 为读入端口选择赋值
        baud_come = self.baud_choose.currentText() # 为波特率选择赋值
        self.read_btn.setEnabled(False) # 设置为不可点击
        self.come_com_choose.setEnabled(False)
        self.thread_2 = In()
        self.thread_2.start()
        # with open('./output.txt','r') as f:
        #     self.textbrowser.clear()
        #     data = f.read()
        #     self.textbrowser.append(data)

    # 定义更改函数
    def change(self):
        self.thread_3 = Ini()
        self.thread_3.start()

    # 定义打开文件夹函数
    def open(self):
        self.thread_4 = Open()
        self.thread_4.start()

    # 定义输出刷新函数
    def Brush_output(self):
        with open('./5500A.txt','r') as g:
            self.textbrowser.clear()
            date = g.read()
            self.textbrowser.append(date)

    # 定义输入刷新函数
    def Brush_input(self):
        with open('./output.txt','r') as f:
            self.textbrowser.clear()
            data = f.read()
            self.textbrowser.append(data)

# 页面加载
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mywindow()
    w.ui.setWindowTitle('5500A')
    w.ui.show()
    app.exec()