import os
import logging
import yaml


try:
    with open(os.environ['CONFIG_PATH']) as file:
        config = yaml.safe_load(file)
except FileNotFoundError:
    logging.error(f"No such file or directory: {os.environ['CONFIG_PATH']})")
    raise BrokenPipeError(f"No such file or directory: {os.environ['CONFIG_PATH']})")
except KeyError:
    logging.error("No directory for utils (CONFIG_PATH) in environment given.")
    raise BrokenPipeError("No directory for utils (CONFIG_PATH) in environment given.")

similar_account = config["similar_account"]
chrome_driver_path = config["chrome_driver_path"]
delay = config["delay"]
scroll_delay = config["scroll_delay"]
config_type = config["config_type"]


if config['account_type'] == 'test':
    email = config["email_test"]
    password = config["password_test"]
    username = config["username_test"]
elif config['account_type'] == 'real':
    email = config["email_real"]
    password = config["password_real"]
    username = config["username_real"]
else:
    raise Exception("Account Type is invalid.")