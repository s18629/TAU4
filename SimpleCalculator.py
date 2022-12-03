class Calculator:
    def __init__(self, first_number, second_number, third_number, example_string):
        self.first_number: float = first_number
        self.second_number: float = second_number
        self.third_number: float = third_number
        self.example_string: str = example_string

    def sum(self) -> float:
        return self.first_number + self.second_number + self.third_number

    def multiply(self):
        return self.first_number * self.second_number * self.third_number

    def subtraction(self):
        return self.first_number - self.second_number - self.third_number


    def add_numbers_to_list(self):
        number_list = list()
        number_list.append([self.first_number, self.third_number])
        return number_list

    def add_string_to_list(self):
        string_list = list()
        string_list.append(self.example_string)

        return string_list

