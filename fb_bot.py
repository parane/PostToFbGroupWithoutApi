
import selenium
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import argparse
import time

# Uncomment this for invisible browser
# display = Display(visible=0)
# display.start() credit Chirag Rathod (Srce Cde) Email: chiragr83@gmail.com



class FbBot():

    def __init__(self, driver, username, password):

        self.driver = driver
        driver.implicitly_wait(10)
        login = self.driver.find_element_by_id("email")
        login.send_keys(username)
        login = self.driver.find_element_by_id("pass")
        login.send_keys(password)
        login.send_keys(Keys.RETURN)

        if driver.current_url != "https://www.facebook.com/":
            exit("Invalid Credentials")
            self.driver.quit()
        else:
            print("Login Successful")

        self.wish_birthday()
        time.sleep(5)
        #self.thanks_like()

    def automate_status(self, URL):
        self.driver.get(URL)
        

        login = self.driver.find_element_by_name("xhpc_message_text")
        login.send_keys("Hi Friends !!! This is testing post in group !!! ")
        self.driver.implicitly_wait(50)
        time.sleep(6)
        login = self.driver.find_element_by_css_selector("._1mf7")
        login.click()
        time.sleep(7)
        self.driver.refresh()
        time.sleep(20)

    def automate_likes(self, URL):
        self.driver.get(URL)
        for i in range(10):

            time.sleep(5)
            get_like_status = self.driver.find_elements_by_css_selector(".UFILikeLink")[i].get_attribute("aria-pressed")
            time.sleep(1)

            if get_like_status == 'false':
                get_like_bt = self.driver.find_elements_by_partial_link_text("Like")
                time.sleep(2)
                get_like_bt[i].click()
                if get_like_bt:
                    print("Done")
                else:
                    print("Not done")

                time.sleep(3)
            else:
                print("Already Liked")
            time.sleep(1800)

    def thanks_like(self):
        count = 0
        profile = self.driver.find_element_by_css_selector('a._2s25')
        time.sleep(5)
        profile.click()
        time.sleep(2)

        profile = self.driver.find_element_by_id('fb-timeline-cover-name').text
        fb_name = profile.split('\n')[0]

        if self.driver.find_element_by_css_selector('.UFIRow.UFILikeSentence._4204._4_dr') or self.driver.find_element_by_css_selector('UFIRow UFIUnseenItem UFILikeSentence _4204 _4_dr'):
            try:
                if self.driver.find_element_by_css_selector('.UFIPagerLink'):
                    time.sleep(1)
                    ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector('.UFIPagerLink')).click().perform()
                    time.sleep(1)
            except:
                pass

            for j in range(len(self.driver.find_elements_by_css_selector('.UFICommentActorName'))):
                if fb_name == self.driver.find_elements_by_css_selector('.UFICommentActorName')[j].text:
                    count += 1

            if count == 0:
                profile = self.driver.find_element_by_css_selector(".UFIAddCommentInput")
                ActionChains(self.driver).move_to_element(profile).click().perform()

                time.sleep(1)
                profile = self.driver.switch_to.active_element

                time.sleep(1)
                profile.send_keys("Thanks for likes")
                time.sleep(3)
                profile.send_keys(Keys.ENTER)
                print("Posted...")
                time.sleep(1)

        else:
            print("Error")

    def wish_birthday(self):
        self.driver.get("https://www.facebook.com/events/birthdays")

        s = self.driver.find_elements_by_name('message')
        print(len(s))
        for i in range(len(s)):
            try:
                wish = self.driver.find_element_by_name('message')
                time.sleep(3)
                wish.send_keys("Boom! Happy Birthday!")
                time.sleep(3)
                wish.send_keys(Keys.ENTER)
                time.sleep(5)
            except:
                pass

            try:
                wish = self.driver.find_element_by_name('message_text')
                time.sleep(3)
                wish.send_keys("Boom! Happy Birthday!")
                time.sleep(3)
                wish.send_keys(Keys.ENTER)
                time.sleep(5)
            except:
                pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--a', help="status or likes?")
    parser.add_argument('--u', help="Username")
    parser.add_argument('--p', help="Password")
    parser.add_argument('--url', help="User/Group URL to perform like")

    args = parser.parse_args()

    if not args.a:
        exit("Please specify status or likes to automate using --a=parameter(status/likes)")
    if not args.u:
        exit("Please specify FB username using --u=parameter")
    if not args.p:
        exit("Please specify FB password using --p=parameter")

    try:
        print("started");
		
        driver = webdriver.Chrome(executable_path=r'C:\python\chromedriver\chromedriver.exe')
        driver.get("https://www.facebook.com/")
       
        f = FbBot(driver, args.u, args.p)
        driver.implicitly_wait(100)
        print("started2");
        if args.a == "status":
            if args.url:
                pass
            
            with open('quote.txt', 'r') as r:
              get_line = sum(1 for line in open('quote.txt'))
              
              for i in range(get_line):
                read_line = r.readline()
                f.automate_status(read_line)
  

        if args.a == "likes":
		
            if args.url:
                url = args.url
                f.automate_likes(url)
            else:
                url = "https://www.facebook.com/"
                f.automate_likes(url)

        print("Thanks for using!!!")

    except KeyboardInterrupt:
        exit("User Aborted")

    except BaseException as e:
        exit("Invalid parameter\nIt should be status or likes"+str(e))

if __name__ == "__main__":
    main()
