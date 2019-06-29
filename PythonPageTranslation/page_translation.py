from selenium import webdriver

# chromedriverのPATHを指定（本ファイルと同じフォルダの場合）
driver_path = './chromedriver' 

# Windows
# driver_path = r'./chromedriver.exe'

# Chrome起動
driver = webdriver.Chrome(driver_path)

# Googleにアクセス
driver.get('http://localhost:8000/')

# Chromeを終了
# driver.quit()