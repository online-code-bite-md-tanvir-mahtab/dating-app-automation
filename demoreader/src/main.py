# from traceback import print_tb
from os import name
from time import sleep
from traceback import print_tb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

edge_path = "G:\edgedriver_win64\msedgedriver.exe"
# creating the webdriver
driver = webdriver.Edge(executable_path=edge_path)

# we need to access the url
driver.get(url="https://eu1.badoo.com/")
FB_NAME = "01955005706#@"
FB_PASWORD = "01955005706#@"

sleep(2)
# we are going to store the current window as the main window
main_page = driver.current_window_handle


login_button = driver.find_element_by_css_selector(" .sign-flow__promo .sign-flow__buttons a")
print(login_button.text)

login_button.click()
base_page = driver.window_handles[0]
login_page = driver.window_handles[1]
driver.switch_to.window(login_page)

print(driver.title)
name_input = driver.find_element_by_xpath(xpath='//*[@id="email"]')
name_input.send_keys(FB_NAME)
password_input = driver.find_element_by_xpath(xpath='//*[@id="pass"]')
password_input.send_keys(FB_PASWORD)
password_input.send_keys(Keys.ENTER)
# driver.close()
# sleep(3)
sleep(8)
driver.switch_to.window(base_page)
print("the main page",driver.title)


sleep(8)

for _ in range(10):
    deslike = driver.find_element_by_xpath(xpath='//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[2]/div[1]')
    # print("the button",deslike.text)
    sleep(2)
    deslike.click()
    print("clicked")
    sleep(2)
sleep(3)







# we need to always close the driver
driver.close()