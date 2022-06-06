from TwitterFollower import TwitterFollower
import os
import twitter_follower.utils.config as config

USERNAME = os.getenv("TWITTER_EMAIL")
PASSWORD = os.getenv("TWITTER_PASSWORD")
SIMILAR_ACCOUNT = config.similar_account
CHROME_DRIVER_PATH = config.chrome_driver_path


if __name__ == "__main__":
    bot = TwitterFollower(CHROME_DRIVER_PATH)
    bot.login(USERNAME, PASSWORD)
    # bot.find_followers(SIMILAR_ACCOUNT)
    bot.find_following(SIMILAR_ACCOUNT)
    # bot.follow()


