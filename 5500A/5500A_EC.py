import serial
try:
    ser = serial.Serial(port='COM1', baudrate='9600')
    print('1')
except:
    print('2')

# class Out(QThread): # 输出数据子进程
#
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         i = 1
#         while i < 255:
#             try:
#                 file = open('./5500A.txt')
#                 ser = serial.Serial(port=com_send , baudrate=baud_send)
#                 ser.isOpen()
#                 ser.write('REMOTE\r\n'.encode('utf-8'))
#                 time.sleep(0.1)
#                 ser.write('*CLS\r\n'.encode('utf-8'))
#                 time.sleep(0.1)
#                 ser.write(('*SRE 8\r\n').encode('utf-8'))
#                 time.sleep(0.1)
#                 ser.write('LIMIT33MA,-33MA\r\n'.encode('utf-8'))
#                 time.sleep(0.1)
#                 for f in file:
#                     ser.write('OUT{0}\r\n'.format(f).encode('utf-8'))
#                     time.sleep(0.2)
#                 ser.write('STOP\r\n'.encode('utf-8'))
#                 break
#             except:
#                 pyautogui.alert('串口连接失败，请检查串口')
#                 break
#         i += 1