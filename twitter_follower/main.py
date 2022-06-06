from TwitterFollower import TwitterFollower
import twitter_follower.utils.config as config

EMAIL = config.email
PASSWORD = config.password
SIMILAR_ACCOUNT = config.similar_account
CHROME_DRIVER_PATH = config.chrome_driver_path


if __name__ == "__main__":
    bot = TwitterFollower(CHROME_DRIVER_PATH)
    bot.login(EMAIL, PASSWORD)
    if config.config_type == 1:
        bot.find_following(SIMILAR_ACCOUNT)
        bot.follow_and_scroll("Following")
    elif config.config_type == 2:
        bot.find_followers(SIMILAR_ACCOUNT)
        bot.follow_and_scroll("Followers")
    else:
        raise Exception("Config type is invalid.")


