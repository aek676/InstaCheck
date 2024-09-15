#instaspy
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from User import User

class instaspy:
    def __init__(self, username, password, target_username):
        self.username = username
        self.password = password
        self.target_username = target_username
        self.browser = webdriver.Firefox(options=Options())

    def login(self):
        browser = self.browser
        browser.implicitly_wait(5)

        #opening instagram.com
        browser.get('https://www.instagram.com/')
        
        #-------click cookies botton
        cookies_button = browser.find_element(By.XPATH, "//button[text()='Decline optional cookies']").click()

        #-------login process starts
        #finding input boxes for username and password and pasing the appropriate values
        browser.find_element(By.XPATH, "//input[@name='username']").send_keys(self.username)
        browser.find_element(By.XPATH, "//input[@name='password']").send_keys(self.password)
        #findind login button and clicking it
        sleep(1)
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        #-------login process ends

    def target_profile(self):
        browser = self.browser
        browser.implicitly_wait(5)

        # #Clicking "Not Now" in pop up just after login
        # sleep(4)
        # not_now_button = browser.find_element(By.XPATH, "//button[text()='Not Now']")
        # sleep(1)
        # not_now_button.click()


        #-------search for victim's username starts
        #click search bar
        sleep(1)
        browser.find_element(By.XPATH, "//span[text()='Search']").click()
        #enter victim's username and clicking Search
        browser.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(self.target_username)
        sleep(3)
        #open victim's profile
        browser.find_element(By.XPATH, "//span[text()='"+self.target_username+"']").click()
        sleep(2)
        #-------search for username stops


    def list_followers(self):
        browser = self.browser
        browser.implicitly_wait(5)

        #clicking and opening followers tabs and getting maximum numbers of followers
        max = int(browser.find_element(By.CSS_SELECTOR, 'a[href*="/followers/"] span[title]').get_attribute('title'))
        browser.find_element(By.CSS_SELECTOR, 'a[href*="/followers/"]').click()
        sleep(2)

        # followersList = browser.find_element(By.CSS_SELECTOR, 'div[role=\'dialog\'] ul')
        followersList = (browser.find_elements(By.CSS_SELECTOR, '.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1sxyh0.xurb0ha.x1uhb9sk.x6ikm8r.x1rife3k.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1'))[-1]
        numberOfFollowersInList = len(followersList.find_elements(By.XPATH, './div'))
        temp = [numberOfFollowersInList, 0]
        # followersList.click()
        
        # actionChain = webdriver.ActionChains(browser)
        while (numberOfFollowersInList < max):
            # actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            last_child = followersList.find_elements(By.XPATH, './div')[-1]
            browser.execute_script("arguments[0].scrollIntoView(true);", last_child)
            sleep(1)
            numberOfFollowersInList = len(followersList.find_elements(By.XPATH, './div'))
            sleep(1)
            if (numberOfFollowersInList == temp[1]):
                break
            else:
                temp[1] = temp[0]
                temp[0] = numberOfFollowersInList

        followers = []
        for user in followersList.find_elements(By.XPATH, './div'):
            # userLink = user.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            userLink = user.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            try:
                img = user.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
            except:
                img = None
                continue
            username = user.find_element(By.CSS_SELECTOR, '._ap3a._aaco._aacw._aacx._aad7._aade').text
            name = user.find_element(By.CSS_SELECTOR, '.x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft').text

            followers.append(User(username, name, img, userLink))
            if (len(followers) == max):
                break

        return followers

    def list_following(self):
        browser = self.browser
        browser.implicitly_wait(5)

        browser.get("https://www.instagram.com/"+self.target_username+"/")
        #clicking and opening following tabs and getting maximum numbers of following
        # max = int(browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[3]/a[1]/span[1]").text.replace(',',''))
        max = int(browser.find_elements(By.CSS_SELECTOR, '.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs')[2].text)
        # browser.find_element(By.XPATH, "//a[@class='-nal3 '][@href='/"+self.target_username+"/following/']").click()
        browser.find_element(By.CSS_SELECTOR, 'a[href*="/following/"]').click()
        sleep(0.5)

        followingList = browser.find_element(By.CSS_SELECTOR, 'div[role=\'dialog\'] ul')
        numberOfFollowingInList = len(followingList.find_elements(By.CSS_SELECTOR, 'li'))
        temp = [numberOfFollowingInList, 0]
        followingList.click()
        actionChain = webdriver.ActionChains(browser)
        while (numberOfFollowingInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            sleep(1)
            numberOfFollowingInList = len(followingList.find_elements(By.CSS_SELECTOR, 'li'))
            sleep(1)
            if (numberOfFollowingInList == temp[1]):
                break
            else:
                temp[1] = temp[0]
                temp[0] = numberOfFollowingInList

        following = []
        for user in followingList.find_elements(By.CSS_SELECTOR, 'li'):
            # userLink = user.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            userLink = user.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            img = user.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
            username = user.find_element(By.CSS_SELECTOR, '._ap3a._aaco._aacw._aacx._aad7._aade').text
            name = user.find_element(By.CSS_SELECTOR, '.x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft').text
            following.append(userLink)
            if (len(following) == max):
                break
        browser.close()
        return following


if __name__ == '__main__':
    InstaSpy_bot = instaspy('mrr78_02', 'b3zzaza', 'ganchova')
    InstaSpy_bot.login()
    InstaSpy_bot.target_profile()
    followers_list = InstaSpy_bot.list_followers()
    following_list = InstaSpy_bot.list_following()
    with open('followers.csv', 'w') as f1:
        f1.write("Followers list:\n")
        for l1 in followers_list:
            f1.write(l1)
            f1.write('\n')
    with open('following.csv', 'w') as f2:
        f2.write("Following list:\n")
        for l2 in following_list:
            f2.write(l2)
            f2.write("\n")
