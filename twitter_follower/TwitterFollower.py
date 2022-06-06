import time
import twitter_follower.utils.config as config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

DELAY = config.delay
SCROLL_DELAY = config.scroll_delay
username = config.username


class TwitterFollower:
    def __init__(self, path):
        s = Service(executable_path=path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def login(self, email, password):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(DELAY)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                 '2]/div[2]/div/div/div/div[5]/label').send_keys(email)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                 '2]/div[2]/div/div/div/div[6]/div').click()
        time.sleep(DELAY)

        """ CHECKS TO SEE IF PROBLEM ON SECOND SCREEN """
        try:
            self.check_second_screen()
        finally:
            pass

        time.sleep(DELAY)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                 '2]/div[2]/div[1]/div/div/div[3]/div/label').send_keys(password)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                 '2]/div[2]/div[2]/div/div[1]/div/div').click()

    def find_followers(self, target):
        time.sleep(DELAY)
        self.driver.get(f"https://www.twitter.com/{target}/followers")
        print("Finding followers...")

    def find_following(self, target):
        time.sleep(DELAY)
        self.driver.get(f"https://twitter.com/{target}/following")
        print("Finding following...")


    def follow_and_scroll(self, page):
        try:
            self.cookies()
        finally:
            pass
        while True:
            self.follow(page) # follows all on the page
            last_height, new_height = self.scroll_down_page() # scrolls down page
            if new_height == last_height: # checks to see if at end of page
                break


    def follow(self, page):
        # 'page' == "Following" or "Followers"
        time.sleep(SCROLL_DELAY)
        print(f"Following the {page}...")
        count = 0
        while True:
            all_buttons = self.driver.find_elements(By.CSS_SELECTOR, f"[aria-label='Timeline: {page}'] .r-19u6a5r")
            for button in all_buttons:
                if button.text == "Follow":
                    button.click()
                    time.sleep(SCROLL_DELAY-0.9)
                    count += 1
                print(f"Count is {count}")


    def scroll_down_page(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        new_height = self.driver.execute_script("return document.body.scrollHeight")
        return last_height, new_height

    def cookies(self):
        reject_cookies = '//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]/div'
        self.driver.find_element(By.XPATH, reject_cookies).click()
        print("Cookies rejected")

    def check_second_screen(self):
        second_screen_xpath = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/span/span'
        if self.driver.find_element(By.XPATH, second_screen_xpath).text == "Enter your phone number or username":
            self.driver.find_element(By.XPATH,
                                     '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                                     '2]/div[ '
                                     '1]/div/div[2]/label/div/div[2]/div/input').send_keys(username)
            self.driver.find_element(By.XPATH,
                                     '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                                     '2]/div[ '
                                     '2]/div/div').click()
