from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def fastFinger():
	global driver
	driver.get('https://10fastfingers.com/typing-test/vietnamese')
	driver.find_element(By.ID,'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
	time.sleep(3)
	while True:
		inputField = driver.find_element(By.ID,'inputfield')
		word = driver.find_element(By.CLASS_NAME, 'highlight').text
		inputField.send_keys(word)
		inputField.send_keys(' ')
		time.sleep(0.1)

def fastFingerRank():
	global driver
	driver.get('https://10ff.net/login')
	time.sleep(3)
	name = driver.find_element(By.ID,'username')
	name.send_keys('quocpro')
	driver.find_element(By.XPATH,"//input[@value='Enter']").click()


def loginFB():
	global driver
	driver.get('https://www.facebook.com/')
	email = driver.find_element(By.XPATH,"//div[@class ='_6lux']/input[@name ='email']")
	# email = driver.find_element(By.ID,'email')
	email.send_keys('example email')

driverPath = 'D:\Code\Selenium Chrome\chromedriver.exe'
driver = webdriver.Chrome(executable_path = driverPath)

fastFinger()

while True:
	pass