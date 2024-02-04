import unittest as ut
from calculator import Calculator as cal
from utility import input_checker as ich
class Tester(ut.TestCase):
    def test_fun(self, name="mul"):
        tlst = []
        alst = []
        with open("u_t_" + name + ".txt", "r") as a:
            text = a.read()
            tlst = text.split("\n")
        with open("u_a_" + name + ".txt", "r") as a:
            text = a.read()
            alst = text.split("\n")
        for i in range(0, len(alst)):
            self.assertEqual(float(cal.calculate(ich.action(tlst[i]))), float(alst[i]))


    def test_executener(self):
        lst = ["sub", "mul", "div"]
        for i in lst:
            self.test_fun(name=i)


tester = Tester()
ut.main(tester)
