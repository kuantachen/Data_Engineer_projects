from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})
# options.add_argument('--start-maximized')
# options.add_argument('--incognito')
# options.add_argument('--disable-popup-blocking')

driver = webdriver.Chrome(executable_path='C:/Users/Uratsuki/Desktop/github/Data_Engineer_projects/python_project/chromedriver.exe')

# 內政部不動產時價登錄網網址
url = 'http://plvr.land.moi.gov.tw/DownloadOpenData'

# 城市清單 (台北 A, 新北 F, 桃園 H, 台中 B, 高雄 E)
city_list = ['A', 'F', 'H', 'B', 'E']

# 開啟網頁
def visit():
    driver.get(url)

    sleep(3)

# 篩選資料
def getdata():
    # 點選 "本期下載"
    driver.find_element(by = By.XPATH, value = '//*[@id="ui-id-1"]').click()
    
    sleep(3)

    # 選擇 "csv檔"
    Select(driver.find_element(By.ID, 'fileFormatId')).select_by_value('csv')

    # 點選進階下載
    driver.find_element(By.CSS_SELECTOR, 'input#downloadTypeId2').click()

    sleep(3)

    # 勾選想要的城市的不動產買賣選項
    for i in city_list:
        driver.find_element(By.CSS_SELECTOR, f"input[value = {i}_lvr_land_A").click()

    sleep(3)

# 下載
def download():
    # 點選下載按鈕
    download_botton = driver.find_element(By.CSS_SELECTOR, 'input#downloadBtnId')
    download_botton.click()

    sleep(10)

# 關閉瀏覽器
def close():
    driver.quit()

if __name__ == "__main__":
    visit()
    getdata()
    download()
    close()
