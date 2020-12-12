import os
import re
def chek(file_name):
    # 1
    F=[]
    F.append(b'\xc7.{0,1}\x50\xfe\xff\xff.{0,20}\x00\x00.{0,20}\xeb\x0f')
    # 2 85
    F.append(b'\x8b.{0,10}\xff\xff\x8b\x8d.{0,10}\xff\xff\x03\x8c.{0,1}')
    # 3 85
    F.append(b'\x8b.{0,10}\xff\xff\x8b\x8d\x44\xfe\xff\xff.{0,10}\x8c.{0,1}\x68\xfe')
    # 4 85
    F.append(b'\x8b.{0,5}\xfe\xff\xff\x8b\x8c.{0,1}\x68\xfe\xff\xff')
    # 5 85
    F.append(b'\x8b.{0,5}\xfe\xff\xff\x8b\x8c.{0,1}\x6c\xfe\xff\xff')
    # 6 85
    F.append(b'\x8b.{0,10}\xff\xff\x8b\x8d.{0,10}\xff\xff\x8b\x94.{0,10}\xff\xff\x3b\x94\x8d')
    # 7 85
    F.append(b'\x8b.{0,10}\xff\xff\x8b\x8d.{0,10}\xff\xff\x8b\x94.{0,10}\xff\xff\x89\x94')
    # 8
    F.append(b'\x03\x45')
    # 9
    F.append(b'\x8B.{0,10}\x0F\xAF')
    # 10
    F.append(b'\xc7\x45.{0,10}\x00\x00\x00')
    # 11
    F.append(b'rand')
    # 12
    F.append(b'\xff\x15')
    # 13
    F.append(b'\x9b\x7c\x00\xa1\xd4\xd0\x7c\x00\x50\xe8.{0,1}\xef\xff\xff\x83\xc4\x08')
    # 14
    F.append(b'\x8b\x8d.{0,10}\xfe\xff\xff\x89\x8c.{0,10}\xfe\xff\xff')
    rez=""
    A=[]
    with open(file_name, 'rb') as byte_file:
        full_data = byte_file.read()
        for i in range(len(F)):
            if (re.search(F[i],full_data)):
                rez+="1"
                A.append(1)
            else:
                rez+="0"
                A.append(0)
    #print(file_name,rez)
    return A
for root,dirs,files in os.walk(r"C:\Users\Данил\Desktop\Вирусы проги"):
    for filename in files:
        mas=chek(root + '\\' + filename)