from typing import Text
from selenium import webdriver
from time import sleep
from pyrogram import Client, filters
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.chrome.options import Options
import requests
import os

API_HASH = os.environ['API_HASH'] # Api hash
APP_ID = int(os.environ['APP_ID']) # Api id/App id
BOT_TOKEN = os.environ['TOKEN'] # Bot token

# Running bot
xbot = Client(
    'ImdbBot',
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@xbot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply("Hi !\n\nI am Movie Info Search Bot,\nSend me a movie name to get started.")

@xbot.on_message(filters.text & filters.private)
async def fetch(bot, message):
    url1 = 'https://www.imdb.com/find?q='
    url2 = f'{message.text}'
    url3 = '&ref_=nv_sr_sm'
    url = url1 + url2 + url3
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=chrome-data")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = "/app/.apt/usr/bin/google-chrome"
    browser = webdriver.Chrome(executable_path="/app/.chromedriver/bin/chromedriver", options=chrome_options)
    browser.get(url) 
    browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[1]').click()
    rate = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]')
    print("rate: " + rate.text)
    year = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[1]/span')
    time = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[3]')
    Summary = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[2]')
    print("year: " + year.text + "      time: " + time.text )
    print("summary is: " + Summary.text)
    
    
xbot.run()
