import pytest

@pytest.fixture()
def before():
    print("------>before函数")


@pytest.mark.usefixtures("before")
class Test_ABC():

    # 函数级开始
    def setup(self):
        print("------->setup")
    def test_a(self):
        print("------->test_1")

    def test_b(self):
        print("------->test_2")

if __name__ == '__main__':
    pytest.main("-s test04_fixture.py")