import time
import pyperclip
import pygetwindow as gw

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

# 브라우저 창을 숨기려면 headless를 사용하여야 하지만 headless를 활성화 한 상태로 브라우징 하면 네이버에서 차단하는 것을 확인함.
# headless 대신 pygetwindow를 사용하여 창을 숨김처리 하는 방식을 채택

# Selenium 옵션 설정
options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
mobile_emulation = {"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
options.add_experimental_option("mobileEmulation", mobile_emulation)
bot = webdriver.Chrome(service=Service(CM().install()), options=options)

# pygetwindow 옵션 설정
#window = gw.getWindowsWithTitle("Chrome")[0]
#window.minimize()  # 최소화
#window.hide()      # 완전히 숨기기

def naver_login(username, password):
	print("입력 받은 정보로 네이버 로그인을 시작합니다.")

	# 로그인 URL 선언
	login_url = "https://nid.naver.com/nidlogin.login"
	parameter = "?svctype=262144" # 모바일 로그인 GET 파라미터

	# 로그인 URL 이동
	bot.get(login_url + parameter)
	time.sleep(2)

	# 페이지에서 상호작용할 입력 칸 및 버튼 정의
	username_input = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_item_id"]')))
	password_input = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_item_pw"]')))
	login_button = WebDriverWait(bot, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit_btn"]')))

	# 네이버 아이디를 클립보드에 담은 후 input 입력칸을 클릭해서 붙여넣기
	pyperclip.copy(username)
	username_input.click()
	actions = ActionChains(bot)
	actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
	time.sleep(1)

	# 네이버 아이디를 클립보드에 담은 후 input 입력칸을 클릭해서 붙여넣기
	pyperclip.copy(password)
	password_input.click()
	actions = ActionChains(bot)
	actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
	time.sleep(1)

	# 로그인 버튼 클릭하기
	login_button.click()
	time.sleep(1)

	# 로그인 버튼 클릭 후 로그인 URL에서 벗어났는지 체크 (벗어난 경우 로그인에 성공)
	if bot.current_url != login_url: # 로그인 체크에서는 GET Parameter가 POST Parameter 로 바뀌기 떄문에 GET 파라미터 없이 비교
		return True
	else:
		return False

# 로그인할 아이디 비밀번호 입력받기
naver_username = input("네이버 아이디 입력: ")
naver_password = input("네이버 비밀번호 입력: ")

if naver_login(naver_username, naver_password) is True: # 로그인 체크에서는 GET Parameter가 POST Parameter 로 바뀌기 떄문에 GET 파라미터 없이 비교
	print("네이버 로그인이 완료되었습니다.")
else:
	print("네이버 로그인에 실패했습니다, 아이디와 비밀번호를 다시 확인해주세요.")