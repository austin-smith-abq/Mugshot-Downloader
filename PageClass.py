from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def init_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    return driver

driver = init_driver()

@dataclass
class MDC():
    id: str
    link: str
    url: str = 'https://gtlinterface.bernco.gov'
    mugshot_img: str = 'img-fluid'

    def get_mugshot(self):
        driver.get(f'{self.url}{self.link}')
        elem = driver.find_element(By.CLASS_NAME, self.mugshot_img)
        elem.screenshot(f'mugshots/{self.id}.png')
