import pytest
from pythoncode.calculator import Calculator
class TestCalc():
    def setup_method(self):
        print("开始计算method")

    @classmethod
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    @classmethod
    def teardown_class(self):
        print("\n结束计算")
    def teardown_method(self):
        print("结束计算method")
    @pytest.mark.parametrize("a,b,expect",[(3,5,8),(-1,-2,-3),(100,200,300)],ids=["int","minus","bigint"])
    def test_add(self,a,b,expect):
        assert expect == self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,expect", [(5, 3, 2), (-5, -2, -3), (300, 200, 100)], ids=["int", "minus", "bigint"])
    def test_sub(self,a,b,expect):
        assert expect == self.calc.sub(a,b)

    @pytest.mark.parametrize("a,b,expect",[(5,2,10),(5.5,10,55),(100,20,2000)],ids=['int','float','bigint'])
    def test_mul(self,a,b,expect):
        assert expect == self.calc.mul(a,b)

    @pytest.mark.parametrize("a,b,expect",[(10,2,5),(10.2,2,5.1),(2000,20,100)],ids=['int','float','bigint'])
    def test_div(self,a,b,expect):
        assert expect == self.calc.div(a,b)
