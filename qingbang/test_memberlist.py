#用户列表
from selenium import webdriver
import unittest
import time
from QW import Login
class Test_user(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.base_url='https://pre.ahqyc.com'

    def test_user(self):
        driver=self.driver
        driver.get(self.base_url)
        # 获取当前句柄
        handle=driver.current_window_handle
        print(handle)
        # 调用登录页面
        Login().user_login(driver)
        # 获取所有的句柄
        handles=driver.window_handles
        url=driver.current_url
        print(url)
        # 验证登录信息的title
        self.assertEqual((driver.title), '青网控股')
        # 切换到新的地址页面
        driver.switch_to_window(handles[-1])
        # 定位用户列表
        driver.find_element_by_xpath('//*[@id="manage"]/ul/li[3]/div').click()
        driver.find_element_by_xpath('//*[@id="manage"]/ul/li[3]/ul/li').click()
        time.sleep(3)
        # 验证电话号码搜索功能
        lists=['18667028576','110','','19999999999']
        test=[]
        for list in lists:
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/input').clear()
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/input').send_keys(list)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/div[7]/button/span').click()
            time.sleep(1)
            # 验证搜索结果信息准确
            texts=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[4]/div/span').text
            test.append(texts)

            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/input').clear()
        print(test)
        values = ['共 1 条', '共 0 条', '共 0 条', '共 1 条']
        dicts=dict(zip(test,values))
        for k,v in dicts.items():
            print(k)
            print(v)
            self.assertEqual(k,v,msg='you are wrong')

    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    main()

