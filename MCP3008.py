--coding:utf-8--
 import spidev
 import time
 spi = spidev.SpiDev() 
 spi.open(0,0)
 def MCP(kanal):
      spi.max_speed_hz = 10000
      ad_num=(8+kanal)<<4
      #0b0000 1000 8
      #0b1000 0000 128
      adc = spi.xfer2([1,ad_num,0])
      data = ((adc[1]&3) << 8) + adc[2]
      #0bxxxx xxxx
      #0b0000 0011
      #0b0000 00xx
      return data
 while True:
     value = MCP(0) 
     print(value)
     time.sleep(0.1)
