import undetected_chromedriver as uc
import time

driver = uc.Chrome()
driver.get("https://www.google.com")



time.sleep(30)

driver.save_screenshot("image.png")
driver.quit()