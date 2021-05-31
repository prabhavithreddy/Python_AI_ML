class Problem:
    '''Program to find triplets whose sum is 0 and print them'''
    
    def get_triplets(self, numbers: int):
        if not numbers or len(numbers) < 3:
            return ()
        triplets = []

        for i in range(0, len(numbers) -2):
            for j in range(i+1, len(numbers) -1):
                for k in range(j+1, len(numbers)):
                    if numbers[i] + numbers[j] + numbers[k] == 22:
                        triplets.append((numbers[i] ,numbers[j], numbers[k]))

        return triplets

    def get_triplets1(self, numbers, sum):
        if not numbers or len(numbers) < 3:
            return ()
        triplets = []

        for i in range(0, len(numbers)-1):
            current_sum = sum - numbers[i]
            s = set()
            for j in range(i+1, len(numbers)):
                if current_sum - numbers[j] in s:
                    triplets.append((numbers[i], numbers[j], current_sum - numbers[j]))
                s.add(numbers[j])

        return triplets

if __name__ == '__main__':
    print(Problem().get_triplets1([1, 4, 45, 6, 10, 8, 12, 2], 22))