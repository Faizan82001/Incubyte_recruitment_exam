import string
import re


class StringCalculator:
    def __init__(self) -> None:
        self.alphabets = list(string.ascii_letters)
        self.sum = 0
        self.negative_numbers = []

    def change_delimiter(self, string_numbers, odd_or_even=None):
        """Change the delimiter from any other value to `,`"""
        delimiter, string_numbers = string_numbers.split('\\n', 1)
        delimiter = delimiter[2:]
        string_numbers = string_numbers.replace(delimiter, ',')
        string_numbers.split(',')
        self.increase_sum(string_numbers, odd_or_even)

    def increase_sum(self, string_numbers, odd_or_even=None):
        """Increase sum of `self.sum` depending upon the odd_or_even parameter"""
        if odd_or_even == None:
            for i in string_numbers:
                if '-' in i:
                    self.negative_numbers.append(i)
                if i.isalpha():
                    self.sum += self.alphabets.index(i) + 1
                elif i.isnumeric():
                    if int(i) <= 1000:
                        self.sum += int(i)
        elif odd_or_even == 'o':
            lis = [string_numbers[i]
                   for i in range(len(string_numbers)) if string_numbers[i].isalnum()]
            for i in range(len(lis)):
                if '-' in lis[i]:
                    self.negative_numbers.append(lis[i])
                if lis[i].isalpha() and i % 2 != 0:
                    self.sum += self.alphabets.index(lis[i]) + 1
                elif lis[i].isnumeric() and i % 2 != 0:
                    if int(lis[i]) <= 1000:
                        self.sum += int(lis[i])
        elif odd_or_even == 'e':
            lis = [string_numbers[i]
                   for i in range(len(string_numbers)) if string_numbers[i].isalnum()]
            for i in range(len(lis)):
                if '-' in lis[i]:
                    self.negative_numbers.append(lis[i])
                if lis[i].isalpha() and i % 2 == 0:
                    self.sum += self.alphabets.index(lis[i]) + 1
                elif lis[i].isnumeric() and i % 2 == 0:
                    if int(lis[i]) <= 1000:
                        self.sum += int(lis[i])

    def add(self, string_numbers) -> int:
        """Driver function for `StringCalculator class`"""
        if string_numbers == '':
            self.sum = 0
        else:
            if len(string_numbers) == 1:
                if string_numbers.isalpha():
                    self.sum += self.alphabets.index(string_numbers) + 1
                else:
                    self.sum += int(string_numbers)
            else:
                if string_numbers.startswith('//'):
                    self.change_delimiter(string_numbers)
                elif string_numbers.startswith('0//'):
                    self.change_delimiter(string_numbers, odd_or_even='o')
                elif string_numbers.startswith('1//'):
                    self.change_delimiter(string_numbers, odd_or_even='e')
                else:
                    # if input is not used the code would be as follows:
                    # string_numbers = re.split(
                    #     ",|\\n|;|/|:|@|%|^|#|&|$|!|[|]", string_numbers)

                    # if input is used the code would be as follows:
                    string_numbers = re.split(
                        r",|\\n|;|/|:|@|%|^|#|&|$|!|[|]", string_numbers)
                    self.increase_sum(string_numbers)

        if self.negative_numbers != []:
            return "Negatives not allowed: \t" + ",".join(self.negative_numbers) + " passed."
        else:
            return self.sum


if __name__ == '__main__':
    user_input = str(input("Enter String here: "))
    string_calculator = StringCalculator()
    ans = string_calculator.add(user_input)
    print(ans)
