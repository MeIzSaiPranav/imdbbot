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
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    browser.get(url)
    therealname = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/h1').text
    imdb250topm = []
    imdb250series = []
    browser.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
    xpath1 = '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr['
    for i in range(1,251):
        pone = str(i)
        ptwo = ']/td[2]/a'
        xpath2 = pone + ptwo
        xpath = xpath1 + xpath2
        name = browser.find_element_by_xpath(xpath)
        imdb250topm.append(name.text)
    browser.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')
    xpath4 = '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr['
    for i in range(1,251):
        pone = str(i)
        ptwo = ']/td[2]/a'
        xpath2 = pone + ptwo
        xpath = xpath4 + xpath2
        name = browser.find_element_by_xpath(xpath)
        imdb250series.append(name.text)

    try:
        browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[1]').click()
        rate = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]')
        print("rate: " + rate.text)
        year = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[1]/span')
        time = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[3]')
        Summary = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[2]')
        print("year: " + year.text + "      time: " + time.text )
        print("summary is: " + Summary.text)
        if therealname in imdb250topm :
            xpath1 = '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/div[2]/div[2]/div['
            for i in range(1,8):
                pone = str(i)
                ptwo = ']'
                xpath2 = pone + ptwo
                xpath = xpath1 + xpath2
                actors = browser.find_element_by_xpath(xpath)
                print('actors: ' + actors.text)
                sleep(1)
            topchecker = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[1]/div')
            print(topchecker.text)
    except Exception:
         browser.get(url)
         browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[1]').click()
         year = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[2]/span')
         time = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[4]')
         Summary = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[1]')
         print("year: " + year.text + "      time: " + time.text )
         print("summary is: " +Summary.text)
         rate = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]')
         print("rate: " + rate.text)
         if therealname in imdb250series:
             xpath1 = '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[5]/div[2]/div[2]/div['
             for i in range(1,8):
                 pone = str(i)
                 ptwo = ']'
                 xpath2 = pone + ptwo
                 xpath = xpath1 + xpath2
                 actors = browser.find_element_by_xpath(xpath)
                 print('actors: ' + actors.text)
             sleep(1)
             topchecker = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[1]/div')
             print(topchecker.text)
    
xbot.run()
