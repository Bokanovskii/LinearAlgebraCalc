from typing import Optional

class Matrix:

    def __init__(self, n, m, nums: list):
        self.rows = n
        self.columns = m
        self.nums = nums
        self.row_lists = self.generate_row_list(n, m, nums)
        self.column_lists = self.generate_column_list(n, m, nums)

    def __repr__(self):
        Mat = ""
        nums = self.nums
        nums_index = 0
        for n in range(self.rows):
            for m in range(self.columns):
                Mat += str(nums[nums_index]) + ", "
                nums_index += 1
            Mat += "\n"
        Mat = Mat[:-3]
        Mat += ";"
        return Mat
    
    def __eq__(self, other):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.row_lists[i][j] != other.row_lists[i][j]:
                    return False
        return True

    def generate_row_list(self, n, m, nums):    
        rows = []
        current_row = []
        nums_index = 0
        for i in range(n):
            rows.append([])
            current_row = rows[i]
            for _ in range(m):
                current_row.append(nums[nums_index])
                nums_index += 1
        return rows

    def generate_column_list(self, n, m, nums): 
        columns = []
        current_column = []
        nums_index = 0
        j = 0
        for i in range(m):
            columns.append([])
            current_column = columns[i]
            for j in range(n):
                if i == 0:
                    current_column.append(nums[m * j])
                if i != 0:
                    current_column.append(nums[i + (j * m)])
        return columns

def product(B, A):
# note that this doesn't check if it is able to be multiplied 
# I want this implimented in the GUI
    nums = []
    for i in range(B.rows):
        for j in range(A.columns):
            nums.append(dot_product(B.row_lists[i], A.column_lists[j]))
    Mat = Matrix(B.rows, A.columns, nums)
    return Mat

def vector_projection(w_vector, x_vector):
# note that this doesn't check if vectors are 2x1
# I want this implimented in the GUI
    mat_scaler = 1/(w_vector.nums[0]**2 + w_vector.nums[1]**2)
    a = w_vector.nums[0]**2
    b = w_vector.nums[0] * w_vector.nums[1]
    c = b
    d = w_vector.nums[1]**2
    nums = [(a/mat_scaler), (b/mat_scaler), (c/mat_scaler), (d/mat_scaler)]
    proj_Mat = Matrix(2, 2, nums)
    return product(proj_Mat, x_vector)

def vector_reflection(w_vector, x_vector):
# note that this doesn't check if vectors are 2x1
# I want this implimented in the GUI
    mat_scaler = 1/(w_vector.nums[0]**2 + w_vector.nums[1]**2)
    a = (w_vector.nums[0]**2) - (w_vector.nums[1]**2)
    b = 2 * (w_vector.nums[0] * w_vector.nums[1])
    c = b
    d = (w_vector.nums[1]**2) - (w_vector.nums[0]**2)
    nums = [(a/mat_scaler), (b/mat_scaler), (c/mat_scaler), (d/mat_scaler)]
    reflect_Mat = Matrix(2, 2, nums)
    return product(reflect_Mat, x_vector)

def add(A, B):
    if len(A.nums) != len(B.nums): raise SizeError
    new_nums = []
    for i in range(len(A.nums)):
        new_nums.append(A.nums[i] + B.nums[i])
    return Matrix(A.rows, A.columns, new_nums)

# implimented to perform matrix products
def dot_product(row, col):
    sum = 0
    for i in range(len(row)):
        sum += row[i] * col[i]
    return sum
