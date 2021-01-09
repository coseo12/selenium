from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://naver.com")

browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[3]/div/div[2]/a").click()

username_input = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/form/fieldset/div[1]/div[1]/span/input")
password_input = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/form/fieldset/div[2]/div[1]/span/input")
login_btn = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/form/fieldset/input")

username_input.send_keys(input("What is your id?"))
password_input.send_keys(input("What is your password?"))
login_btn.click()