from TwitterFollower import TwitterFollower
import os

USERNAME = os.getenv("TWITTER_EMAIL")
PASSWORD = os.getenv("TWITTER_PASSWORD")
SIMILAR_ACCOUNT = "DrSimEvans"
CHROME_DRIVER_PATH = "C:/Users/dunca/OneDrive/Python/chromedriver/chromedriver.exe"



bot = TwitterFollower(CHROME_DRIVER_PATH)

bot.login(USERNAME, PASSWORD)
# bot.find_followers(SIMILAR_ACCOUNT)
bot.find_following(SIMILAR_ACCOUNT)
# bot.follow()


