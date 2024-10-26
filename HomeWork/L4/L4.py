from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import tensorflow as tf
# 設置 TensorFlow 的日誌級別
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 只顯示錯誤信息


chromedriver_path = "./chromedriver.exe"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)


driver.get('https://24h.pchome.com.tw/')
# driver.maximize_window() # 最大化視窗
time.sleep(1)


def auction_1():

    while True:

        try:

            keyword = input('請輸入手機商品關鍵字: ')
            
            
            while True:
                sort_method = int(input('請輸入數字: 1:推薦排行、2:新上架、3:價格 : '))
                if sort_method in [1,2,3]:
                    break
                else:
                    print('請輸入數字 1,2,3')
             
            # 預先清除輸入框的數字
            driver.find_element(By.XPATH,("//input[@type='search']")).clear() 
            # 輸入文字到輸入框
            driver.find_element(By.XPATH,("//input[@type='search']")).send_keys(keyword)
            time.sleep(1)
            # 點擊鍵盤 enter
            driver.find_element(By.XPATH,("//input[@type='search']")).send_keys(Keys.ENTER)
            time.sleep(1)
            # 選擇手機平板
            driver.find_element(By.XPATH,("//div[text()='手機/平板']")).click()
            time.sleep(1)
            # 選擇手機
            driver.find_element(By.XPATH,("//div[text()='手機']")).click()
            time.sleep(1)

            break

        except ValueError:
            print("輸入無效，請輸入一個整數。")  # 捕獲 ValueError 並提示用戶

        except Exception as e:    
            print('無法搜尋到手機/平板相關資訊，請重新輸入關鍵字')
            auction_1()
    
    auction_2(sort_method)


def auction_2(sort_method):
    # 1:推薦排行、2:新上架、3:價格
    if sort_method == 1:
        sort_method_str = '推薦排行'
        driver.find_element(By.XPATH,('//span[text()="推薦排行" and @class="btn__text"]')).click()
        time.sleep(1)       

    elif sort_method == 2:
        sort_method_str = '新上架'
        driver.find_element(By.XPATH,('//span[text()="新上架" and @class="btn__text"]')).click() 
        time.sleep(1)       

    elif sort_method == 3:
        sort_method_str = '價格'
        driver.find_element(By.XPATH,('//span[text()="價格" and @class="btn__text"]')).click() 
        time.sleep(1)

    time.sleep(2)
    lowerPrice = driver.find_element(By.XPATH,("(//div[@class='c-prodInfoV2__priceValue c-prodInfoV2__priceValue--m'])[1]")).text
    goodsName = driver.find_element(By.XPATH,("//div[@class='c-prodInfoV2__title'][1]")).text
    print(f'依據{sort_method_str}排序結果:')
    print(f'搜尋結果:第一個商品名稱: "{str(goodsName)}"\n第一個商品價格: "{str(lowerPrice)}"')


auction_1()



