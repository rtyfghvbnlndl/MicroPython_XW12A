### XW12A driver for MicroPython.
### 驱动芯网xw12a 触摸ic

## Example:
```python
from xw12a import xw12a

a=xw12a(scl=16,sda=18,freq=400000,ASEL='N')
raw_list = a.read()
#[False, False, Ture, False, False, False, False, False, False, False, False, False, False, False, False, False]
num_list=a.read_list()
#[2]
```
## Function Parameters 参数
scl=16 use GPIO16 as SCL  
sda=18 use GPIO18 as SDA  
freq=400000  frequency is 400kHz  
ASEL='N' ASEL is Floating

### ASEL List
ASEL is a pin of xw12a.The address of xw12a varies with electrical level of ASEL.  
不同地址对应的ASEL值
|  ASEL   | 7bit addr  | ASEL= |
|  ----  | ----  | ----  |
|  Floating悬空 | 0x40 | ASEL='N' |
| GND  | 0x42 |ASEL='L'|
| VDD  | 0x44 | ASEL='H'|

它不是标准的i2c，直接用machine的i2c没跑起来，甚至scan()不到地址。头秃
