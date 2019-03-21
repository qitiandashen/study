from selenium import webdriver
import unittest
import time
from QW import Login
class test_addmember(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.base_url = 'https://pre.ahqyc.com'
    def test_add(self):
        driver=self.driver
        driver.get(self.base_url)
        # 获取当前句柄
        handle=driver.current_window_handle
        # 调用登录页面
        Login().user_login(driver)
        # 获取所有的句柄
        handles=driver.window_handles
        # 验证登录信息的title
        self.assertEqual((driver.title), '青网控股')
        # 切换到新的地址页面
        driver.switch_to_window(handles[-1])
        driver.find_element_by_xpath('//*[@id="manage"]/ul/li[3]/div').click()
        driver.find_element_by_xpath('//*[@id="manage"]/ul/li[3]/ul/li').click()
        time.sleep(3)
        # 添加企业

        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/button/span').click()

        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').click()
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[4]/span').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div[1]/input').send_keys('测试专用')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[3]/div/div[1]/input').send_keys('14411111111')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/div[3]/div/button[2]/span').click()

    def tearDown(self):
        self.driver.close()
if __name__=='__main__':
    maiin()
