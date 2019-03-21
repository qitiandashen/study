from selenium import webdriver
import unittest
import time
from QW import Login
class Addbill(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url='http://192.168.2.7/#/'
    def test_add(self):
        driver=self.driver
        driver.get(self.base_url)
        '''调用登录'''
        Login().user_login(driver)

        handles1=driver.window_handles
        # 验证登录信息的title
        self.assertEqual((driver.title), '青网控股')
        # 切换到新的地址页面
        driver.switch_to_window(handles1[-1])
        driver.find_element_by_xpath('//*[@id="manage"]/ul/li[3]/div').click()
        driver.find_element_by_xpath('//*[@id="manage"]/ul/li[3]/ul/li').click()
        time.sleep(3)
        # 添加账单
        driver.find_element_by_xpath('//*[@id="manage"]/ul/li[8]/div').click()
        driver.find_element_by_xpath('//*[@id="manage"]/ul/li[8]/ul/li[2]').click()
        #获得新的句柄
        handles2=driver.window_handles
        driver.switch_to_window(handles2[-1])
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/button/span').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/div/div/input').send_keys('liu123（未来已来）')
        driver.find_element_by_xpath('')



