from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import base64

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def Login():
    # 打开网站
    driver.get("http://litemall.hogwarts.ceshiren.com/vue/index.html#/login?redirect=user")
    time.sleep(1)
    # 填充用户名
    driver.find_element_by_css_selector("#app > div.login.view-router > div.field_group > div:nth-child(1) > div.md_field_control > input[type=text]").send_keys("reliable")
    time.sleep(1)
    # 填充密码
    driver.find_element_by_css_selector("#app > div.login.view-router > div.field_group > div:nth-child(2) > div.md_field_control > input[type=password]").send_keys("success01")
    # 点击登录
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/button').click()
    time.sleep(1)
    driver.find_element_by_css_selector("#app > div.van-hairline--top-bottom.van-tabbar.van-tabbar--fixed > div:nth-child(1) > div.van-tabbar-item__icon > i").click()
    time.sleep(1)
    driver.find_element_by_class_name('van-field__control').click()
    time.sleep(1)
    driver.find_element_by_class_name('van-field__control').send_keys("火焰杯测试商品")
    time.sleep(1)
    driver.find_element_by_class_name('van-field__control').send_keys(Keys.ENTER)
    time.sleep(1)
    #加入购物车  //*[@id="app"]/div[2]/div[2]/div[1]/div/div/div[1]/div

    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div/div/div[1]/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('// *[ @ id = "app"] / div[2] / div[5] / button[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[3]/div[3]/button[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[5]/div[1]/div').click()

if __name__ == "__main__":
    Login()
