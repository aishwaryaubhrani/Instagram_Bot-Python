from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:
    def __init__(self, username,  password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password  = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        bot.find_element_by_class_name('HoLwm').click()
        time.sleep(6)
    def likePost(self, hashtag):
        bot = self.bot
        bot.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(5)
        for i in range(0,6):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            post = bot.find_elements_by_tag_name('a')
            links = [elem.get_attribute('href') 
                    for elem in post]
            for link in links:
                bot.get(link)
                try:
                    bot.find_element_by_class_name('afkep').click()
                    time.sleep(5)
                except Exception as e:
                    print("cannot like")
ob = InstaBot('the_holycoder', 'makhalamdang12')
ob.login()
ob.likePost('javascript')