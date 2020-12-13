import pytest
from pythoncode.calculator import Calculator
class TestCalc():
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")
    def teardown_class(self):
        print("\n结束计算")
    @pytest.mark.parametrize("a,b,expect",[(3,5,8),(-1,-2,-3),(100,200,300)],ids=["int","minus","bigint"])
    def test_add(self,a,b,expect):
        assert expect == self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,expect", [(5, 3, 2), (-5, -2, -3), (300, 200, 100)], ids=["int", "minus", "bigint"])
    def test_add(self,a,b,expect):
        assert expect == self.calc.sub(a,b)