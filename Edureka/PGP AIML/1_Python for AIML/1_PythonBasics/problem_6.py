class Problem:
    '''Program that accepts N values and print it as a list'''
    
    def get_list(self, numbers: str):
        if not numbers:
            return []
        return [int(number) for number in numbers.split()]

if __name__ == '__main__':
    print(Problem().get_list("1 2 3 4 5"))