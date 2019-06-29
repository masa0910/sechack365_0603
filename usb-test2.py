# 2モードでなんとかしたい(新規登録:ret/ 検出:det)
# python usb-test2.py [実行モード]
# で実行してください
# DBとの連携とかは現状触ってないです、どう処理させましょう…?

from selenium import webdriver
import win32com.client
import time
import sys
import db_access

from win10toast import ToastNotifier 

driver_path = './PythonPageTranslation/chromedriver'

#繋がっているデバイスのリストを更新
def get_devinfo(dev_list, sta):
    #wmiを使ってdeviceidを取得
    wmi = win32com.client.GetObject ("winmgmts:")
    for usb in wmi.InstancesOf ("Win32_USBHub"):
        if usb.DeviceID.split("\\")[2] not in dev_list:
            #初期デバイスリストの作成(DB使うときは、ここにDBのリストを引っ張ってくる(今ある処理を消すと、ハブとかが引っかかるので注意))
            if sta == 0:
                dev_list.append(usb.DeviceID.split("\\")[2])
            #初回のリスト作成以外で新規のデバイスが見つかったとき
            else:
                #新規デバイスを返り値とする
                return usb.DeviceID.split("\\")

def main():
    dev_list = []               #新規デバイス検知用のリスト(既存のデバイスを抱えるための)
    for obj in db_access.call():
        dev_list.append(str(obj))
    #初期デバイスリストの作成
    get_devinfo(dev_list, 0) 
    print(str(dev_list))
    
    while 1:
        #デバイスリストの更新
        new_dev = get_devinfo(dev_list, 1)
        #Noneが帰ってくる = 新規デバイスなし/None以外が帰ってくる = 新規デバイスがnew_devに格納されている
        if new_dev != None:
            #print("new device : "+str(new_dev[2]))
            print("new device : "+str(new_dev))
            #regモード(新規デバイス登録モード)起動時
            if sys.argv[1] == "reg":
                permit_reg = input("allow ...add new device? (y or n) :" )
                if permit_reg == "y":
                    dev_list.append(new_dev)
                    print("add : new divice"+str(new_dev[2]))
                    sys.argv[1] = "det"
                    continue
            #pidとvidが欲しい貴方に
            if sys.argv[1] == "reg_django":
                print("pid : "+str(new_dev[1][4:8])+" vid : "+str(new_dev[1][13:17]))
                input()
            
            #detモード(新規デバイス検出)起動時
            if sys.argv[1] == "det":
                ###何か新しいデバイスあるよ!!!っていうところ
                ###他と組み合わせてエラー画面とか吐かせたいですね

                #print("not allow ...new divice : "+str(new_dev[2]))
                
                toaster = ToastNotifier()
                toaster.show_toast("not registered usd detect!!! ", "未登録のUSBは使用できません\n "+str(new_dev), duration=10) 
                
                input()

                driver = webdriver.Chrome(driver_path)
                driver.get('http://localhost:8000/')
        #次回処理までの待ち時間設定(sec)
        time.sleep(1)
   
if __name__ == "__main__":
    main()
