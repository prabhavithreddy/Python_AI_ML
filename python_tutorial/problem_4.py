class Problem4:
    '''Write a program to generate N numbers of fibbonacci seris'''
    
    def generate_fibonacci(self, number: int):
        numbers = []
        if number<1:
            return numbers
        sum = 0
        a = 0
        b = 1
        numbers.append(a)
        while sum < number:
            numbers.append(b)
            sum = a + b
            a = b
            b = sum
        return numbers

if __name__ == '__main__':
    print(Problem4().generate_fibonacci(20))