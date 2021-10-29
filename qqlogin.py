from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
with Chrome(options=options) as driver:
  driver.get('https://www.baidu.com/')