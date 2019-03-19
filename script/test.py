from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(10)


driver.find_element_by_id("kw").send_keys("blue")

action = ActionChains(driver)

el = driver.find_element_by_css_selector("/html/body/div[1]/div[5]/div[1]/div[3]/div[2]/h3/a/em")
action.context_click()
action.perform()



