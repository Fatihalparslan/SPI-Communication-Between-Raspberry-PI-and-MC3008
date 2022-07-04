# SPI-Communication-Between-Raspberry-PI-and-MC3008

### ENABLING SPI INTERFACE AND INSTALLING SPI LIBRARY 

sudo raspi-config

                 |
                 
                 |--->Interfacing Options
                 
                                         |
                                        
                                         |-->SPI
                                         
                                                |
                                                
                                                |->Would you like the SPI interface to be enabled?(YES)
                                                
 sudo reboot
 
 sudo apt-get update
 
 sudo apt-get upgrade
 
 sudo apt-get install -y python-dev python3-dev
 
 sudo apt-get install -y python-spidev python3-spidev
 
 sudo apt install git
 
 git clone https://github.com/Gadgetoid/py-spidev.git
 
 cd py-spidev
 
 sudo python setup.py install
 
 sudo python3 setup.py install
 
 spiDev Komutları
 
 open(bus, device)
 
 Yukarıdaaki komut ls /dev/spi komutu girildiğinde /dev/spidev. formatında çıkan bus üzerinden device cihazlarına erişimi sağlar.Bu komut ile 
 master cihazımızın spi cihazı kullanıma açarız.
 
 readbytes(n)
 Yukarıdaaki komut ile spi bufferında n byte kadar veri okuruz. Eğer bufferda veri yoksa bu komut veri gelmesini bekler.
 
 writebytes(list of values)
 Yukarıdaaki komut list içindeki değerleri 8 bit olarak sırayla gönderir.
 
 writebytes2(list of values)
 
 Bu fonksiyonun writebytes fonksiyonundan farkı verilerin fiziksel olarak gönderilmeden önce tutulduğu bufferın hafıza kapasitesini aşan miktarda veriler 
 gönderilmesini sağlar.
 
 xfer(list of values)
 
 Yukarıdaki fonksiyon list içindeki verileri yazarken aynı zamanda veri de okur.Yazma işlemi bittiğinde okuma da biter. 
 her veri bloğu gönderiminin sonunda CS pini serbest bırakılır.
 
 xfer2(list of values)
 
 list elemanlarının gönderimi bitmeden veri bloğu serbest kalmaz.
 
 xfer3(list of values)
 bufferın hafıza kapasitesini aşan miktarda veriler gönderilmesini sağlar.
 
 close()
 
 Yukarıdaki fonksiyon  spi cihazını kullanıma kapatır.
 
