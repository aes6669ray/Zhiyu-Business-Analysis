from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

path="爬蟲\chromedriver.exe"
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True) #不要讓網頁自己關閉
driver = webdriver.Chrome(chrome_options=option)

driver.get("https://course-tvc.yuntech.edu.tw/web_nu/search_course.aspx")
driver.maximize_window()
time.sleep(2)

select = Select(driver.find_element(By.NAME,'ctl00$QueryPH$SearchBar_Course1$YearDDL'))
select.select_by_index(1)


select2 = Select(driver.find_element(By.NAME,'ctl00$QueryPH$SearchBar_Course1$TermDDL'))
select2.select_by_index(0)

input= driver.find_element(By.XPATH,'//*[@id="ctl00_QueryPH_SearchBar_Course1_SBI0_TB"]')
input.send_keys("人工智慧")

login=driver.find_element(By.XPATH,'//*[@id="ctl00_QueryPH_SearchBar_Course1_SubmitQueryBtn"]')
login.click()


schn=WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_RightFramePH_SchoolList1_SchoolListLV_ctrl3__SchoolName"]'))
    )

schn.click()

time.sleep(2)

title=driver.find_elements(By.CLASS_NAME,"list-content")
tp=[]

for i in title:
    tp.append(i.text)

print(tp)

time.sleep(2)

nextp=driver.find_element(By.XPATH,'//*[@id="ctl00_RightFramePH_CourseList1_CourseDataPager"]/a[4]')
nextp.click()

time.sleep(2)

title=driver.find_elements(By.CLASS_NAME,"list-content")

tp2=[]

for i in title:
    tp2.append(i.text)

print(tp2)

# time.sleep(2.5)
# nextp=driver.find_element(By.XPATH,'//*[@id="ctl00_RightFramePH_CourseList1_CourseDataPager"]/a[8]')
# nextp.click()
# time.sleep(2)

# title3=driver.find_elements(By.CLASS_NAME,"list-content")
# tp3=[]

# for i in title3:
#     tp3.append(i.text)

# print(tp3)

# driver.close()


#如果遇到捲動式網頁 需要執行捲動才能載入更多網頁資訊的話可以執行javascript的語法控制網頁再來爬資料
#drive.execute_script("Window.scrollTo(0,document.body.scrollHeight);")
#time.sleep(2) #等兩秒鐘讓資料讀出來
