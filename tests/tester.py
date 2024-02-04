import unittest as ut
from calculator import Calculator as cal
from utility import input_checker as ich
class Tester(ut.TestCase):
    def test_fun(self, name="add"):
        tlst = []
        alst = []
        with open("test_tesxts/u_t_" + name + ".txt", "r") as a:
            text = a.read()
            tlst = text.split("\n")
        with open("test_tesxts/u_a_" + name + ".txt", "r") as a:
            text = a.read()
            alst = text.split("\n")
        for i in range(0, len(alst)):
            self.assertEqual(round(float(cal.calculate(ich.action(tlst[i]))), 2), round(float(alst[i]), 2))


    def test_executener(self):
        lst = ["sub", "mul", "div", "pow", "fnc"]
        for i in lst:
            self.test_fun(name=i)


tester = Tester()
ut.main(tester)
