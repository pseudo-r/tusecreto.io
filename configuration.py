import time
from tus_secretos import * 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

age = 22
post_text = 'Testing para saber si tu mama es maraca'
bot = tusecretoBot(age, post_text)

for i in range (3):
    bot.post(age, post_text)
    age = age + 1
    print (age)
