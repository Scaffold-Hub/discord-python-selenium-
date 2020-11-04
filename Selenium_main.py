from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
from Email_password import email,password
import time


class Discord:
    
    def __init__(self, email,password):
        self.email = email,password
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('../Bots/Agario/chromedriver.exe', chrome_options=self.browserProfile)

    def signIn(self):
        self.browser.get('https://discord.com/login?redirect_to=%2Fchannels%2F%40me')
        time.sleep(2)

        emailInput = self.browser.find_element_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input")

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
class Process:
    def __init__(self):
        def change_pp(self, profile):
            self.profile = profile
            profileInput = self.browser.find_element_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div/div/nav/div[2]/div[1]/div/div[2]/div/svg/foreignObject/a/div/svg/path")
            profileInput.send_keys(self.profile)
            profileInput.click()

            def settings(self,Settings):
                self.Settings = Settings

                SettingsInput = self.browser.find_element_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div/div/div/div/div[1]/section/div[2]/div[3]/button[3]/div/svg/path")
                SettingsInput.send_keys(self.Settings)
                SettingsInput.click()

            def edits(self,Edits):
                self.Edits = Edits

                EditsInput = self.browser.find_element_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div[2]/div/div[2]/div/div/main/div/div[1]/div/div/button/div")
                EditsInput.send_keys(self.Edits)
                EditsInput.click()

            def change_pp(self,Change):
                self.Change = Change
                ChangeInput = self.browser.find_element_by_xpath("//*[@id='pp-mount']/div[2]/div/div[2]/div[2]/div/div[2]/div/div/main/div/div[1]/div/div/div[1]/div[1]/div[1]/div/input")
                ChangeInput.send_keys(self.Change)
                ChangeInput.click()

                x, y = pyautogui.locateCenterOnScreen("desktop.png")
                pyautogui.click(x, y)
                x, y = pyautogui.locateCenterOnScreen("file0.png")
                pyautogui.click(x, y)
                x, y = pyautogui.locateCenterOnScreen("file.png")
                pyautogui.click(x, y)
                x, y = pyautogui.locateCenterOnScreen("file2.png")
                pyautogui.click(x, y)


dscrd = Discord(email,password)
prcss = Process()
dscrd.signIn()