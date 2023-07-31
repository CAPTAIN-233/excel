# def readTxt():
#     data = []
#     with open("5500A.txt","r") as f:
#         for line in f.readlines():
#             line = line.strip("\n")
#             line = line.split()
#             data.append(line)
#     print(data)
#     return data


# import serial
# import serial.tools.list_ports
#
# ports_list = list(serial.tools.list_ports.comports())
# if len(ports_list) <= 0:
#     print('no')
# else:
#     print('yes')
#     for comport in ports_list:
#         print(list(comport)[0], list(comport)[1])

# import serial
#
# ser = serial.Serial(port='COM1', baudrate=115200)
# write_len = ser.write('114514'.encode('utf-8'))
#
# ser.close()

file = open(r'./5500A.txt', 'r')
for f in file:
    print(f,end='')


