#!/usr/bin/python
import sys
import usb.core
import time

def get_devs(devices):
    # find USB devices
    dev = usb.core.find(find_all=True)
    # loop through devices, printing vendor and product ids in decimal and hex
    for cfg in dev:
        #sys.stdout.write('Decimal VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct) + '\n')
        #sys.stdout.write('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n') 
        
        #登録済デバイスかの判定/追加
        if cfg.idProduct not in devices:
            print("new device")
            devices.append(cfg.idProduct)
                
if __name__ == "__main__":
    devices = []    #取得済デバイス管理用配列
    while 1:
        #繋がっている(繋げたことのある)デバイスの取得と配列表示
        get_devs(devices)
        print(devices)
        time.sleep(5)