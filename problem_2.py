class Problem2:
    '''Write a program to create a list of even numbers starting from x to y'''
    
    def get_event_numbers(self, start, end):
        numbers = []
        if not start and not end:
            return numbers
        if start%2 != 0:
            start = start+1
        for number in range(start, end+1, 2):
            numbers.append(number)
        return numbers


if __name__ == '__main__':
    print(Problem2().get_event_numbers(1, 20))