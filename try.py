# from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# display = Display(visible=0, size=(800, 600))
# display.start()

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_experimental_option("debuggerAddress",f"localhost:8989")
driver = webdriver.Chrome(options=options)

try:
    # driver.get('https://www.linkedin.com/')
    # driver.find_element(by=By.XPATH,value=f'/html/body/main/section[1]/div/div/form[1]/div[1]/div[1]/div/div/input').send_keys('manojtomar326@gmail.com')
    # driver.find_element(by=By.XPATH,value=f'/html/body/main/section[1]/div/div/form[1]/div[1]/div[2]/div/div/input').send_keys('Tomar@@##123')
    # driver.find_element(by=By.XPATH,value=f'/html/body/main/section[1]/div/div/form[1]/div[2]/button').click()
    # print(driver.page_source)
    # driver.refresh()
    # print(driver.title)
# Switch to the iframe element
    iframe_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
    driver.switch_to.frame(iframe_element)

    # Locate the button element inside the iframe and click it
    iframe_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
    driver.switch_to.frame(iframe_element)

    # Locate the button element inside the iframe and click it
    iframe_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
    driver.switch_to.frame(iframe_element)

    # Locate the button element inside the iframe and click it
    iframe_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
    driver.switch_to.frame(iframe_element)

    driver.page_source
    # Locate the button element inside the iframe and click it
    iframe_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
    driver.switch_to.frame(iframe_element)

    button_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div/div[3]/div/ul/li[2]/a")))
    button_element.click()
finally:
    driver.quit()
    # display.stop()