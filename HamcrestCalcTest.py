from hamcrest import *
import unittest
import SimpleCalculator
from SimpleCalculator import Calculator

calc = Calculator(1, 5, 7.7, 'example')

class TestCalc(unittest.TestCase):
    def testEquals(self):
        assert_that(calc.sum(), equal_to(13.7))

    def testLength(self):
        assert_that(calc.add_numbers_to_list(), has_length(1))

    def testClassInstance(self):
        assert_that(calc, instance_of(object))

    def testvalueCloseTo(self):
        assert_that(calc.sum(), close_to(13.0, 1.0))

    def testContainString(self):
        assert_that(calc.add_string_to_list(), contains('example'))

    def testGreaterThan(self):
        assert_that(calc.multiply(), greater_than(10))

    def testGreaterThanOrEquals(self):
        assert_that(calc.multiply(), greater_than_or_equal_to(10.4))

    def testContainInList(self):
        assert_that(calc.add_string_to_list(), has_item('example'))

