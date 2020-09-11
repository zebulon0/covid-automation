"""
file: covid_automation.py
author: Zeb Hollinger | zah1276@rit.edu

description: Python script that automates the covid daily
             check-ins for RIT Ready and ATS

"""

from selenium import webdriver
import yaml
import time

#  vars for the RIT daily check-in
conf = yaml.full_load(open("hidden.yml"))
ritUser = conf["rit_main"]["username"]
ritPassword = conf["rit_main"]["password"]

#  vars for the ATS daily check-in
atsID = conf["rit_ats"]["id"]
atsPassword = conf["rit_ats"]["password"]

#  initialize ChromeDriver
driver = webdriver.Chrome()

#  radio button strings
button1 = "MainContent_RptrAthleteForms_rblYesCHecked_1_1_1"
button2 = "MainContent_RptrAthleteForms_rblYesCHecked_2_1_2"
button3 = "MainContent_RptrAthleteForms_rblYesCHecked_3_1_3"
button4 = "MainContent_RptrAthleteForms_rblYesCHecked_4_1_4"
button5 = "MainContent_RptrAthleteForms_rblYesCHecked_5_1_5"
button6 = "MainContent_RptrAthleteForms_rblYesCHecked_6_1_6"
button7 = "MainContent_RptrAthleteForms_rblYesCHecked_7_1_7"
button8 = "MainContent_RptrAthleteForms_rblYesCHecked_8_1_8"
button9 = "MainContent_RptrAthleteForms_rblYesCHecked_9_1_9"
button10 = "MainContent_RptrAthleteForms_rblYesCHecked_10_1_10"


def login_rit(url, usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_name(submit_buttonId).click()
    driver.get("https://dailyhealth.rit.edu/assessment")
    time.sleep(1)
    driver.find_element_by_xpath("//div[contains(text(), 'NO')]").click()
    time.sleep(1)


def login_ats(url, usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_id(submit_buttonId).click()
    try:
        driver.find_element_by_id("MainContent_RptrAthleteForms_rblYesCHecked_1_1_1")
    except:
        driver.find_element_by_id("cmdScreening").click()
    driver.find_element_by_id(button1).click()
    driver.find_element_by_id(button2).click()
    driver.find_element_by_id(button3).click()
    driver.find_element_by_id(button4).click()
    driver.find_element_by_id(button5).click()
    driver.find_element_by_id(button6).click()
    driver.find_element_by_id(button7).click()
    driver.find_element_by_id(button8).click()
    driver.find_element_by_id(button9).click()
    driver.find_element_by_id("MainContent_btnNextFormPage").click()
    driver.find_element_by_id(button10).click()
    driver.find_element_by_id("MainContent_cmdSaveForms2").click()
    driver.get("https://www.atsusers.com/ATSAthletePhone/Default.aspx?action=logout")
    driver.close()


login_rit("https://dailyhealth.rit.edu/", "username", ritUser, "password", ritPassword, "_eventId_proceed")

login_ats("https://www.atsusers.com/ATSAthletePhone/login.aspx?db=atsrit", "txtUserName", atsID, "txtPassword",
          atsPassword, "cmdLogin")
