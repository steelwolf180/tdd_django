from selenium import webdriver

browser = webdriver.Firefox(executable_path='../../geckodriver')
browser.get('http://127.0.0.1:8000')

assert 'successfully' in browser.title
