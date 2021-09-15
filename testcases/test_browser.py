from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class PracticeSelenium():

    def test1(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        #   https://jqueryui.com/droppable/
        #   https://courses.letskodeit.com/practice
        driver = webdriver.Firefox(executable_path='./../drivers/geckodriver.exe')
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)
        element = driver.find_element(By.ID,"mousehover")
        itemToClickLocator = "//*[@id='mousehover']"
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            topLink = driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            print("Item Clicked")
        except:
            print("Mouse Hover failed on element")
        # driver.switch_to.frame(0)
        # fromElement = driver.find_element(By.ID, 'draggable')
        # toElement = driver.find_element(By.ID, 'droppable')
        # time.sleep(2)
        # try:
        #     actions = ActionChains(driver)
        #     actions.drag_and_drop(fromElement, toElement).perform()
        #     print('Drag and drop successful')
        #     time.sleep(2)
        # except:
        #     print("Drag and drop failed")
        finally:
            driver.close()

        # driver.find_element(By.ID, "name").send_keys("Anil")
        # driver.find_element(By.ID, "alertbtn").click()
        # time.sleep(2)
        # alert1 = driver.switch_to.alert
        # alert1.accept()
        # time.sleep(2)
        # driver.find_element(By.ID, "name").send_keys("Anil")
        # driver.find_element(By.ID, "confirmbtn").click()
        # time.sleep(2)
        # alert2 = driver.switch_to.alert
        # alert2.dismiss()
        #


ff = PracticeSelenium()
ff.test1()
