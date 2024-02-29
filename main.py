from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

url = 'https://kirbycafe-reserve.com/guest/tokyo/reserve/'

driver.get(url)
time.sleep(10)
print("kirbycafe-reserve.com connected!")

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div/div[2]/button').click()
time.sleep(1)
print("kirbycafe-reserve.com select warning button!")

driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[1]').click()
print("kirbycafe-reserve.com select menu button!")
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="list-35"]/div[2]').click()
print("kirbycafe-reserve.com select menu button!")
time.sleep(10)

board = []
table = driver.find_element(By.XPATH, '//*[@id="calendar-scroller"]/table')
tbody = table.find_element(By.TAG_NAME, 'tbody')
rows = tbody.find_elements(By.TAG_NAME, "tr")

board.append(["time", "3", "4", "5", "6"])
    
    
for index, value in enumerate(rows):
    tmp = []
    time = value.find_element(By.TAG_NAME, "th")
    tmp.append(time.text)
    array = value.find_elements(By.TAG_NAME, "td")
    for i in range(2, 6): # 3, 4, 5, 6
        tmp.append(array[i].text)
    board.append(tmp)

for b in board:
    print(b)