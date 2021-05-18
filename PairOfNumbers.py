def get_indices(array, target):
    l = 0
    h = len(array) - 1
    while l < h:
        if array[l] + array[h] == target:
            return (l, h)
        l += 1
        h -= 1
    return None

def get_indices1(array, target):
    indices = []
    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            if array[i] + array[j] == target:
                indices.append([i, j])
    return indices

def get_indices2(array: list, target):
    indices = []
    array.sort()
    for i in range(len(array)):
        current_diff = target - array[i]
        if current_diff in array[i:]:
            indices.append([i, array.index(current_diff)])
    return indices

def get_indices2(array: list, target):
    indices = []
    s = set()
    for i in range(len(array)):
        current_diff = target - array[i]
        if current_diff in s:
            indices.append([i, array.index(current_diff)])
        s.add(array[i])
    return indices

print(get_indices2([10,20,10,40,50,60,70], target=90))