import SimpleCalculator
from SimpleCalculator import Calculator

if __name__ == '__main__':
    calc = Calculator(1, 2, 3.4, 'example')
    print(calc.sum())
    print(calc.multiply())
    print(len(calc.add_numbers_to_list()))
    print(calc.add_string_to_list())
    print(calc.add_string_to_list())
