from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
def zijie():
    # 打开网站
    driver.get("https://jobs.bytedance.com/campus/position")
    time.sleep(1)
    # #bd > section > section > main > div > div > div.header__36dmY > div > div.search-block.searchBlock__1mh35 > span > input
    driver.find_element_by_css_selector("#bd > section > section > main > div > div > div.header__36dmY > div > div.search-block.searchBlock__1mh35 > span > input").send_keys("测试")
    time.sleep(2)
    driver.find_element_by_css_selector("#bd > section > section > main > div > div > div.header__36dmY > div > div.search-block.searchBlock__1mh35 > span > input").send_keys(Keys.ENTER)
    time.sleep(2)
    #判断查到的第一个结果有没有测试这个词
    message = driver.find_element_by_css_selector('#bd > section > section > main > div > div > div.content__IN8vJ > div.rightBlock.rightBlock__2ZGFh > div.borderContainer__3S4gr > div.listItems__1q9i5 > a:nth-child(1) > div > div.title__37NOe.positionItem-title.sofiaBold > span').text
    # 判断如果有这个文本信息，那么布尔值是真的，否则就是假的
    # print(type(message))
    # print(len(message))
    result = "测试" in message
    if (result):
        print("搜索的结果中 包含测试这个词！")
    else:
        print("搜索的结果中 不包含测试这个词！")
if __name__ == '__main__':
    zijie()