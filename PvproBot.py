from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

import pyttsx3
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
class PvproBot:
    def __init__(self):
        self.driver=webdriver.Chrome("C:/Users/KIIT/Downloads/chromedriver.exe")
        self.driver.get("https://www.pvpro.com/game/public")
        sleep(8)
        self.driver.find_element_by_xpath("//button[contains(text(), 'No Thanks')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Login')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div/div/div[7]/div[1]/div/div[1]/div/form/div[3]/img").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys('YOUR_STEAM_USERNAME')
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys('YOUR_STEAM_PASSWORD')
        sleep(2)
        #self.driver.find_element_by_xpath("//button[contains(text(), 'Login')]").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[2]/div/div[2]/div[2]/div/form[1]/div[4]/input").click()
        speak("please provide the authenticator key")
        sleep(20)
        self.driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/form/div[4]/div[1]/div[1]").click()
        speak("block the notification")
        sleep(10)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/ul/span[4]/span/li").click()
        sleep(2)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Claim Coins')]").click()
            speak("coin collected")
        except Exception as e:
            speak("already collected the coin")
            a=self.driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]/div/div[1]/div/div[1]/div[3]/div").text
            speak(a)
            b=self.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[1]/button/span/span").text
            speak("your total coin is")
            speak(b)
        
        
mybot=PvproBot()
    
   
