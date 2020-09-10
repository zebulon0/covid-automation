from selenium import webdriver
import yaml

#  vars for the rit daily check-in
conf = yaml.load(open("hidden.yml"))
ritUser = conf["rit_main"]["name"]
ritPassword = conf["rit_main"]["password"]

#  vars for the ATS daily check-in
atsUser = conf["rit_sports"]["id"]
atsPassword = conf["rit_sports"]["password"]

#  initialize ChromeDriver
driver = webdriver.Chrome()


# absolute XPATH
# /html/body/div[@id='root']/div[1]/div[@class='ae']/div[@class='af ag ah ai aj ak']/div[@class='al']/div[@class='ai aj
# b0 b1 b2 b3 b4']/div[@class='b5 aj ai b6 b7 b8']/div[@class='b5 bd']/div[@class='ai cx']/div[@class='cy cz d0 d1 d2
# d3 d4 d5 ai aj d6 ca d8 d9']/div[@class='ba at da c4 db']


def login_rit(url, usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_name(submit_buttonId).click()
    driver.get("https://dailyhealth.rit.edu/assessment")
    driver.find_element_by_xpath("//div[contains(text(), 'NO')]").click()

    driver.close()


def login_ats(url, usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_id(submit_buttonId).click()
    # driver.find_element_by_id("cmdScreening").click()
    driver.find_element_by_id("MainContent_RptrAthleteForms_rblYesCHecked_1_1_1").click()
    driver.find_element_by_id("MainContent_RptrAthleteForms_rblYesCHecked_2_1_2").click()
    driver.find_element_by_id("MainContent_RptrAthleteForms_rblYesCHecked_3_1_3").click()
    driver.find_element_by_id("MainContent_RptrAthleteForms_rblYesCHecked_4_1_4").click()
    driver.find_element_by_id("MainContent_RptrAthleteForms_rblYesCHecked_5_1_5").click()
    driver.find_element_by_id("MainContent_RptrAthleteForms_rblYesCHecked_6_1_6").click()
    driver.find_element_by_id("MainContent_RptrAthleteForms_rblYesCHecked_7_1_7").click()
    driver.find_element_by_id("MainContent_RptrAthleteForms_rblYesCHecked_8_1_8").click()
    driver.find_element_by_id("MainContent_RptrAthleteForms_rblYesCHecked_9_1_9").click()
    driver.find_element_by_id("MainContent_btnNextFormPage").click()
    driver.find_element_by_id("MainContent_RptrAthleteForms_rblYesCHecked_10_1_10").click()
    driver.find_element_by_id("MainContent_cmdSaveForms2").click()
    driver.get("https://www.atsusers.com/ATSAthletePhone/Default.aspx?action=logout")
    driver.close()


login_rit("https://dailyhealth.rit.edu/", "username", ritUser, "password", ritPassword, "_eventId_proceed")

# login_ats("https://www.atsusers.com/ATSAthletePhone/login.aspx?db=atsrit", "txtUserName", atsUser, "txtPassword",
          # atsPassword, "cmdLogin")
