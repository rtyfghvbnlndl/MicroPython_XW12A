from machine import Pin, I2C
from time import sleep

class xw12a(object):
    def __init__(self, scl=int, sda=int, freq=400000, ASEL='N'):
        if ASEL=="H":
            self.addr_rw='10001001'
        elif ASEL=="L":
            self.addr_rw='10000101'
        else:
            self.addr_rw='10000001'
        
        self.scl=Pin(scl,mode=Pin.OUT,value=(1))
        self.sda=Pin(sda,mode=Pin.OUT,value=(1))
        self.sda_num=sda
        self.sleep_time=1/freq/2
    
    def start(self):
        self.scl(1)
        self.sda(0)
        sleep(self.sleep_time)
    
    def send(self,data):
        self.scl(0)
        sleep(self.sleep_time)
        if data:
            self.sda(1)
        else:
            self.sda(0)
        self.scl(1)
        sleep(self.sleep_time)

    def stop(self):
        self.scl(0)
        sleep(self.sleep_time)
        self.sda(0)
        self.scl(1)
        sleep(self.sleep_time)
        self.sda(1)

    def listen(self):
        self.scl(0)
        sleep(self.sleep_time)
        self.scl(1)
        sleep(self.sleep_time)
        if self.sda.value():
            return False
        else:
            return True
    
    def read(self):
        alist=[]
        self.start()
        for i in self.addr_rw:
            self.send(int(i))
        self.sda=Pin(self.sda_num,mode=Pin.IN)
        if self.listen():
            print('found')
        else:
            print('erro')
        for i in range(16):
            res = self.listen()
            alist.append(res)
        self.sda=Pin(self.sda_num,mode=Pin.OUT,value=(1))
        self.send(1)
        self.stop()
        return alist

    def read_list(self):
        ft=self.read()
        result=[]
        for i in range(12):
            if ft[i]:
                result.append(i)
        return result
            


if __name__ == '__main__':
    a=xw12a(scl=16,sda=18,freq=400000,ASEL='N')
    while True:
        print(a.read())
        print(a.read_list())
        sleep(1)
