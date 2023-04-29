from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
SearchName= "cleartrip"
search= driver.find_element(By.NAME,"q").send_keys(SearchName)
driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").click()
driver.find_element(By.XPATH,"//*[@id='tads']/div[1]/div/div/div/div[1]/a/div[2]/span[1]/span[2]/span[1]/div/span").click()

driver.find_element(By.XPATH,"//body/div[@class='p-fixed l-0 r-0 b-0 t-0 flex flex-center flex-middle z-70']/div/div[@class='d-flex']/div[2]/div[1]/div[1]/div[2]//*[name()='svg']").click()
driver.find_element(By.XPATH,"//div[@class='ml-4 mr-2 c-secondary-500 fs-4 fw-500 flex flex-1']").click()

driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div/div/button").click()

driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div/div/div/ul/li[2]").click()

driver.find_element(By.XPATH,"//div[contains(@class,'p-relative br-4')]//button[contains(@class,'flex flex-middle flex-between t-all fs-2 focus:bc-secondary-500 bg-transparent bc-neutral-100 c-pointer c-neutral-900')]").click()
driver.find_element(By.XPATH,"//div[@class='ls-reset br-4 w-100p px-2 dropdown__item c-neutral-900 flex flex-between flex-middle px-4']//li[@class='flex-inline']//*[name()='svg']").click()

driver.find_element(By.XPATH,"//div[@class='pt-8 pb-10 p-relative px-10 px-4--xs pt-4--xs pb-4--xs home-search-banner']").click()

driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]").click()

driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[3]").click()
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div/div[1]/input").send_keys("new")
driver.find_element(By.XPATH,"//p[normalize-space()='New Delhi, IN - Indira Gandhi Airport (DEL)']").click()
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div/div[3]/input").send_keys("blr")
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div/div[3]/div[2]/ul/li/div/div[2]").click()
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[4]/div/div[1]/div/div/button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@aria-label='Thu May 18 2023']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[contains(@aria-label,'Sat Jun 17 2023')]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[contains(@class,'flex flex-around ml-6 bg-primary-500 hover:bg-primary-600 c-white bc-transparent c-pointer w-100p py-2 px-5 h-10 fs-4 fw-600 t-all button bs-solid tp-color td-500 bw-1 br-4 lh-solid box-border home-search-btn ml-2--xs')]").click()
time.sleep(10)