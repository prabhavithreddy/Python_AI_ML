class QuickSort:
    def sort(self, numbers, low, high):
        if low < high:
            i = self.partition(numbers, low, high)
            self.sort(numbers, low, i-1)
            self.sort(numbers, i+1, high)

    def partition(self, numbers, low, high):
        pivote = numbers[high]
        i = low-1
        for j in range(low, high):
            if numbers[j] <= pivote:
                i = i+1
                self.swap(numbers, i, j)
        self.swap(numbers, i+1, high)
        return i+1

    def swap(self, numbers, left_index, right_index):
        numbers[left_index], numbers[right_index] = numbers[right_index], numbers[left_index]

if __name__ == '__main__':
    numbers = [10, 7, 8, 9, 1, 5]
    QuickSort().sort(numbers, 0, len(numbers)-1)
    print(numbers)
    # [1,4,3,2,5]
    # [1,2,3,4,5]