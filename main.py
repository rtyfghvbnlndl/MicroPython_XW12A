from xw12a import xw12a
from time import sleep
a=xw12a(scl=16,sda=18,freq=400000,ASEL='N')
while True:
    print(a.read())
    print(a.read_list())
    sleep(0.2)
