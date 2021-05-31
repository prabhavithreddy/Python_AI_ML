class Problem5:
    '''Program to find sum of digit from a given integer number N'''

    def sum_of_digits(self, number: int):
        if number < 0:
            return 0
        sum = 0
        while number > 0:
            digit = number % 10
            sum = sum + digit
            number = number // 10
        return sum

if __name__ == '__main__':
    print(Problem5().sum_of_digits(12345))