from selenium import webdriver
import time

driver = webdriver.Firefox()
l = open("espanhol.txt", 'r')
f = open("espanholsredirect.txt", 'w+')
#driver.get(l.readline())
#print(l.readline())


for x in range(0, 103):
	driver.get(l.readline())
	#time.sleep(5)
	f.write(driver.current_url + '\n')