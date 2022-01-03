from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

DELAY = 3


class TwitterFollower:
    def __init__(self, path):
        s = Service(executable_path=path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def login(self, email, password):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(DELAY)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div['
                                 '1]/div/div[5]/label').send_keys(email)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div['
                                 '1]/div/div[6]/div').click()
        time.sleep(DELAY)

        second_screen_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[' \
                              '1]/div/div[1]/div[1]/span '

        if self.driver.find_element(By.XPATH, second_screen_xpath).text == "Enter your phone number or username":
            self.driver.find_element(By.XPATH,
                                     '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                                     '2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(
                "energy_scouter")
            self.driver.find_element(By.XPATH,
                                     '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                                     '2]/div[2]/div/div').click()
        time.sleep(DELAY)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div['
                                 '1]/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(password)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div['
                                 '2]/div/div').click()

    def find_followers(self, target):
        time.sleep(DELAY)
        self.driver.get(f"https://www.twitter.com/{target}")
        time.sleep(DELAY)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                           '2]/div/div/div[1]/div/div[5]/div[2]/a').click()
        print("Finding followers...")
        self.scroll()

    def find_following(self, target):
        time.sleep(DELAY)
        self.driver.get(f"https://www.twitter.com/{target}")
        time.sleep(DELAY)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                           '2]/div/div/div[1]/div/div[5]/div[1]/a').click()
        print("Finding following...")
        self.scroll()

    def follow(self):
        time.sleep(DELAY)
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "[aria-label='Timeline: Following'] .r-19u6a5r")
        print("Following people...")
        for button in all_buttons:
            print(button.text)
            if button.text == "Follow":
                button.click()
                time.sleep(DELAY)

    def scroll(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight")
            time.sleep(DELAY)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break
            last_height = new_height
