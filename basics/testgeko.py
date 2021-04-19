from selenium.webdriver import Firefox

driver = Firefox(executable_path='./geckodriver')
driver.get("https://selenium.dev")
