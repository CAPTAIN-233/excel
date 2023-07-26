import serial,time
plist = []
qlist = []
ser = serial.Serial(port='COM5', baudrate=9600)
# hexstr = 'EFEF' + '0002080A' +'FFEFFFFF' # 复位
# bytes_hex = bytes.fromhex(hexstr)
# ser.write(bytes_hex)
# time.sleep(5)
hexstr = 'EFEF' + '00050200051E2A' +'FFEFFFFF' # 设置波长
bytes_hex = bytes.fromhex(hexstr)
ser.write(bytes_hex)
for i in range(11):
    read = ser.read()
read = []
time.sleep(3)
hexstr = 'EFEF' + '0003010206' +'FFEFFFFF' # 读取光功率
bytes_hex = bytes.fromhex(hexstr)
ser.write(bytes_hex)
# hexstr = 'EFEF' + '000307000A' + 'FFEFFFFF'  # 虚拟按键
# bytes_hex = bytes.fromhex(hexstr)
# ser.write(bytes_hex)
# time.sleep(0.5)
# hexstr = 'EFEF' + '00020305' + 'FFEFFFFF'  # 查询波长
# bytes_hex = bytes.fromhex(hexstr)
# ser.write(bytes_hex)
# time.sleep(0.5)

for i in range(0,15):
    read = ser.read()
    plist.append(int.from_bytes(read,byteorder='big',signed=False))
    qlist.append(read)
# for i in range(50):
# read = ser.read()

del plist[0:6]
del plist[2:9]
x = format(int(hex(plist[0]),16),'x'); y = format(int(hex(plist[1]),16),'x')
z = x+y
z1 = (int(z,16)-65535) * 0.01 # dbm
z2 = round((10**(z1/10)),1)  # 功率 单位um
print(x,'x')
print(y,'y')
print(z1,'z1')
print(z2,'z2')
print(type(z2),'z2')
print(plist)
print(qlist)