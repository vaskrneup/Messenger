from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import secrets

import random


class Messenger:
    def __init__(self, account_url, messages=None, driver_path="chromedriver.exe"):
        """
        :param account_url: Link to account to whom the message is sent.
        :param messages: List of messages to send, if not provided random chars will be used.
        """
        self.account_url = account_url
        self.messages = messages
        self.current_user_url = None

        # load the login page !
        self.driver = webdriver.Chrome(
            executable_path=driver_path
        )

    def change_message_user(self, account_url):
        self.account_url = account_url
        self.current_user_url = account_url

    def set_messages(self, messages):
        """
        sets messages if not provided initially.
        :param messages: list of messages.
        :return: None
        """
        self.messages = messages

    def login(self, username, password, wait_time=10):
        """
        Logs in to messenger using given credentials.
        * No ERROR is raised if login is unsuccessful.
        :param wait_time: how long to wait for page to load, if not provided default will be used.
        :param username: username of facebook/messenger
        :param password: password of facebook/messenger
        :return: None
        """
        time.sleep(wait_time / 2)
        self.driver.get("https://www.messenger.com/")

        # fills the form to login !!
        # fills username/email field !!
        self.driver.find_element_by_id("email").send_keys(username)
        # wait for half second !!
        time.sleep(0.5)
        # fills password !!
        self.driver.find_element_by_id("pass").send_keys(password)
        # wait
        time.sleep(0.5)
        # click login btn !!
        self.driver.find_element_by_id("loginbutton").click()

        # wait for request to complete !!
        time.sleep(wait_time / 2)

    def __message(self, message, wait_before_next_message):
        # type message !!
        self.driver.find_element_by_css_selector(
            "._1mf"
        ).send_keys(message)
        # wait for some time !!
        time.sleep(wait_before_next_message or 0.1)
        # send message !!
        self.driver.find_element_by_css_selector("._38lh").click()

    def send_message(self, user_page_wait_time=10, message_count=10, use_random_message=False,
                     min_message_length=30, max_message_length=100, wait_before_next_message=0.1):
        """
        :param user_page_wait_time: wait_time: how long to wait for page to load, if not provided default will be used.
        :param wait_before_next_message: how long to wait before sending next message if not provided 0.1 will be used.
        :param min_message_length: minimum message length to send use_random_message is True.
        :param max_message_length: maximum message length to send use_random_message is True.
        :param message_count: Number of message to send if use_random_message is True.
        :param use_random_message: send random message.
        :return: None
        """
        if self.current_user_url != self.account_url:
            self.driver.get(self.account_url)

            # wait for page to load !!
            time.sleep(user_page_wait_time)

        # for sending random message !!
        if use_random_message:
            for _ in range(message_count):
                self.__message(
                    message=secrets.token_urlsafe(random.randint(int(min_message_length), int(max_message_length))),
                    wait_before_next_message=wait_before_next_message
                )
        else:
            # for sending provided messages.
            if self.messages:
                for message in self.messages:
                    self.__message(message=message, wait_before_next_message=wait_before_next_message)
            else:
                raise ValueError(
                    "No Message Provided, you can use set_messages([<MY MESSAGE LIST>]) to provide messages"
                )
        # for sent messages to complete !
        time.sleep(user_page_wait_time / 3)

    def close(self):
        """
        closes the driver
        :return: None
        """
        self.driver.quit()


if __name__ == '__main__':
    # you can copy the url of particular user from messenger.com !!
    # You need to download selenium web driver for this to work !!
    # you can download driver for your preferred browser here:
    # https://selenium-python.readthedocs.io/installation.html
    messenger = Messenger(
        "https://www.messenger.com/t/<USERNAME>",
        driver_path="<DRIVER PATH>"
    )
    # Login Using your facebook credentials !!
    messenger.login("<USERNAME>", "<PASSWORD>")
    # user use_random_message=True to send random message.
    # You can use message count to specify how many message you wish to send.
    messenger.send_message(use_random_message=True, message_count=100)
    # You can also send specific message !!
    messenger.set_messages(["you can", "specify any", "Number of messages."])
    # send the message from set_messages !!
    messenger.send_message()
    # close after everything is completed !!
    messenger.close()
