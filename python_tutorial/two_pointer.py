class TwoPointer:
    def get_pair(self, numbers):
        i = 0
        j = len(numbers) - 1
        while i<j:
            if numbers[i] + numbers[j] == 0:
                print(numbers[i], numbers[j])
                i = i+1
                j = j-1
            elif numbers[i] + numbers[j] < 0:
                i = i+1
            else:
                j = j-1

if __name__ == '__main__':
    numbers = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
    result = TwoPointer().get_pair(numbers)
    print(result)
    # [1,4,3,2,5]
    # [1,2,3,4,5]