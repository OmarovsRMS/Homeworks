class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list
    def __str__(self):
        return f'{self.matrix_list[0]}\n{self.matrix_list[1]}'
    def __add__(self, other):
        new_list = [[],[]]
        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[0])):
                new_list[i].append(self.matrix_list[i][j] + other.matrix_list[i][j])
        return Matrix(new_list)

mtx1 = Matrix([[1,2,3], [2,3,4]])
mtx2 = Matrix([[4,10,1], [4,5,6]])
print(mtx1, '\n')
print(mtx2, '\n')

print(mtx1+mtx2)

