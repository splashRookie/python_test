import sys
import os

from app_automate.Yaml_p1.base.get_driver import get_driver
from app_automate.Yaml_p1.page.page_login import PageLogin

sys.path.append(os.getcwd())





class TestLogin:
    # setup
    def setup(self):
        # 初始化 PageLogin
        self.login = PageLogin(get_driver())

    # teardown
    def teardown(self):
        # 关闭driver
        self.login.driver.quit()

    # 测试方法
    def test_login(self, username="itheima", pwd="123456", expect_result="itheima"):
        # 登录
        self.login.page_login(username, pwd)
        try:
            # 断言
            assert expect_result == self.login.page_get_info()
            try:
                # 退出
                self.login.page_logout()
                # 断言退出是否成功
                assert self.login.page_logout_is_ok()
            except:
                print("退出断言失败")
        except AssertionError as e:
            print("登录断言出错！")