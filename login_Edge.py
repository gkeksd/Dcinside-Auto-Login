import sys, os
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 사용자로부터 ID와 비밀번호를 입력 받음
input_id = input("당신의 디시인사이드 아이디를 입력하세요: ")
input_pw = input("당신의 디시인사이드 비밀번호를 입력하세요: ")

# Microsoft Edge WebDriver 경로 설정
edge_driver_path = os.path.join(sys._MEIPASS, "msedgedriver.exe")  # Edge WebDriver의 경로를 지정하세요
service = EdgeService(edge_driver_path)

# Edge 웹드라이버 실행
driver = webdriver.Edge(service=service)

# 디시인사이드 로그인 페이지 열기
driver.get("https://sign.dcinside.com/login")

# 페이지 로드 대기
time.sleep(3)

# ID 입력
id_auto = driver.find_element(By.CLASS_NAME, 'id')  # 클래스로 요소 찾기
id_auto.send_keys(input_id)

# PW 입력
pw_auto = driver.find_element(By.CLASS_NAME, 'pw')  # 클래스로 요소 찾기
pw_auto.send_keys(input_pw)
pw_auto.send_keys(Keys.ENTER)

# 로그인 후 대기
time.sleep(3)

# 사용자 입력을 대기하여 스크립트가 종료되지 않게 함
input("Press Enter to EXIT and close the browser...")

# 브라우저 종료
driver.quit()
