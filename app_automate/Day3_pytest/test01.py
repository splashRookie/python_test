import pytest


class Test_ABC():
    # 工厂模式
    @classmethod
    def setup_class(cls):
        print("执行setUpClass函数")

    @classmethod
    def teardown_class(cls):
        print("执行tearDownClass函数")
    # 函数级开始
    def setup(self):
        print("------->setup_method")
    # 函数级结束
    def teardown(self):
        print("------->teardown_method")
    def test_a(self):
        print("------->test_a")
        assert 1
    def test_b(self):
        print("------->test_b")
if __name__ == '__main__':
    pytest.main("-s  test01.py")