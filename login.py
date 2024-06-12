from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

input_id = input("당신의 디시인사이드 아이디를 입력하세요: ")
input_pw = input("당신의 디시인사이드 비밀번호를 입력하세요: ")


chrome_driver_path = "chromedriver.exe"
service = Service(chrome_driver_path)

# 웹드라이버 실행
driver = webdriver.Chrome(service=service)

# Instagram 웹사이트 열기
driver.get("https://sign.dcinside.com/login")

# 10초 동안 대기
time.sleep(5)

# ID 입력
id_auto = driver.find_element(By.CLASS_NAME, 'id') # 클래스로 단일 요소 찾기
id_auto.send_keys(input_id)

# PW 입력
pw_auto = driver.find_element(By.CLASS_NAME, 'pw') # 클래스로 단일 요소 찾기
pw_auto.send_keys(input_pw)
pw_auto.send_keys(Keys.ENTER)

# 필요하다면 브라우저를 조금 더 대기시키려면, 시간을 변경하세요.
time.sleep(5)

# 사용자 입력을 대기하여 스크립트가 종료되지 않게 합니다.
input("Press Enter to EXIT and close the browser...")