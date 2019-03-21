# 登录、注册模块封装
class Login():

    def user_login(self,driver):
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/div[1]/div/input').clear()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/div[1]/div/input').send_keys('yansishi')
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/div[2]/div/input').clear()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/div[2]/div/input').send_keys('960807')
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/div[3]/div/button').click()
    def user_logout(self,driver):
        driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/span').click()
        driver.close()


