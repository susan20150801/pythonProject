import time

import pytest
import yaml
from selenium import webdriver

test_data = yaml.safe_load(open("./web/contact.yml", encoding="UTF-8"))
class TestWework():
    @classmethod
    def setup_class(cls):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        cls.driver = webdriver.Chrome(options=opt)
        cls.driver.implicitly_wait(5)
        cls.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        cookie = cls.driver.get_cookies()
        print(cookie)
        with open("./web/data.yml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize("name,accoutNo,telephone",test_data)
    def test_add_members(self,name,accoutNo,telephone):
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        with open("./web/data.yml",encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        time.sleep(2)
        self.driver.find_element_by_link_text('添加成员').click()
        time.sleep(2)
        self.driver.find_element_by_id('username').send_keys(name)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(accoutNo)
        self.driver.find_element_by_id("memberAdd_phone").send_keys(telephone)
        self.driver.find_element_by_link_text("保存并继续添加").click()





#     def test_demo(self):
#         opt = webdriver.ChromeOptions()
#         #设置debugger地址
#         opt.debugger_address = "127.0.0.1:9222"
#         driver = webdriver.Chrome(options=opt)
#         driver.implicitly_wait(5)
#         driver.get('https://work.weixin.qq.com/wework_admin/frame')
#         driver.find_element_by_id("menu_contacts").click()
#         cookie = driver.get_cookies()
#         print(cookie)
# #使用cookies登录
# def test_cookie():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(5)
#     driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
#     cookies = [{'domain': '.qq.com', 'expiry': 1608286407, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850305712065'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'rnH-eOaIH8wR31C0MA4pBDS9cJG4pn_MsleQPelr1M9f1EtgNGFqJKQO3OHfrtbiJQ2ElEoMUfH4RLiaPWr4V8ihmeiG0znL2PR759Mh2wTZ_Ya8viZgdc2ly3GYx7wZ6DdNPLvK4yauh9GIJ5oOLexVmH-A7G3f0k4s_HUp4-qWzTCO71vCANhTmkEKhWucSNOjpPfje_wNr6AEUN2OzlrScMgx9LNA_5uGkumlmNu-qCe0M8US5WMeEnAxnYvwY8OEPm1vZi2EKmpuVCyKWg'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850305712065'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325069199544'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1448224'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s5904658564'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'vqLhzBhKom1eBjmdvN_pec63O-Ki_E3fnZKGRHf1FU6Rukc0MCPht4yelz0Fc7IE'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639822031, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608210330,1608285217,1608285770,1608286032'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '3636443145'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608286032'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '859899002161145'}, {'domain': '.qq.com', 'expiry': 1608372747, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1351395707.1608210306'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608316741, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '1ajn4mu'}, {'domain': '.qq.com', 'expiry': 1671358347, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.738693266.1608210306'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639746268, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1610878347, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
#     for cookie in cookies:
#         driver.add_cookie(cookie)
#     driver.get("https://work.weixin.qq.com/wework_admin/frame")
#     driver.find_element_by_id("menu_contacts").click()
#     time.sleep(2)
#     driver.quit()
#
# def test_get_cookie():
#     opt = webdriver.ChromeOptions()
#     # 设置debug地址
#     opt.debugger_address = "127.0.0.1:9222"
#     driver = webdriver.Chrome(options=opt)
#     driver.implicitly_wait(5)
#     driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
#     cookie = driver.get_cookies()
#     print(cookie)
#     with open("./web/data.yml","w",encoding="UTF-8") as f:
#         yaml.dump(cookie,f)
#
# def test_login():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(5)
#     driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
#     with open("./web/data.yml",encoding="UTF-8") as f:
#         yaml_data = yaml.safe_load(f)
#     for cookie in yaml_data:
#         driver.add_cookie(cookie)
#     driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
#     time.sleep(3)