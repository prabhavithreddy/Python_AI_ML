import numpy as np
def get_range(n=10):
    return np.arange(n)

def multiply(matrix1, matrix2):
    return np.array(matrix1)*np.array(matrix2)

def dot_product(matrix1, matrix2):
    return np.array(matrix1).dot(np.array(matrix2))

print(get_range())
print(multiply([[1,6,5],
                [3,4,8],
                [2,12,3]], [[3,4,6],
                            [5,6,7],
                            [6,56,7]]))
print(dot_product([[1,6,5],
                [3,4,8],
                [2,12,3]], [[3,4,6],
                            [5,6,7],
                            [6,56,7]]))

print(np.array([1.2,1.6,2]).floor())