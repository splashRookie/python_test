import pytest

class Test_1():

    # 函数级开始
    @pytest.mark.run(order=-1)
    def test_a(self):
        print("------->test_a")

    @pytest.mark.run(order=1)
    def test_b(self):
        print("------->test_b")

if __name__ == '__main__':
    pytest.main("test03_order.py")