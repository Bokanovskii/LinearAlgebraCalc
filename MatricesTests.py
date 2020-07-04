import unittest

import Matrices
from Matrices import Matrix


class TestRepr(unittest.TestCase):

    def test_repr_1(self):
        Mat = Matrix(2, 2, [1, 2, 3, 4])
        self.assertEqual(str(Mat), "1, 2, \n3, 4;")


class TestRowLists(unittest.TestCase):

    def test_row_list_1(self):
        Mat = Matrix(2, 2, [1, 2, 3, 4])
        self.assertEqual(Mat.row_lists, [[1, 2], [3, 4]])

    def test_row_list_2(self):
        Mat = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
        self.assertEqual(Mat.row_lists, [[1, 2, 3], [4, 5, 6]])

    def test_row_list_3(self):
        Mat = Matrix(3, 2, [1, 2, 3, 4, 5, 6])
        self.assertEqual(Mat.row_lists, [[1, 2], [3, 4], [5, 6]])

class TestColumnLists(unittest.TestCase):

    def test_column_list_1(self):
        Mat = Matrix(2, 2, [1, 2, 3, 4])
        self.assertEqual(Mat.column_lists, [[1, 3], [2, 4]])
    
    def test_column_list_2(self):
        Mat = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
        self.assertEqual(Mat.column_lists, [[1, 4], [2, 5], [3, 6]])

    def test_column_list_2(self):   
        Mat = Matrix(3, 2, [1, 2, 3, 4, 5, 6])
        self.assertEqual(Mat.column_lists, [[1, 3, 5], [2, 4, 6]])

class TestProduct(unittest.TestCase):
    
    def test_product_1(self):
        B = Matrix(2, 2, [1, 2, 3, 4])
        A = Matrix(2, 2, [5, 6, 7, 8])
        B_x_A = Matrix(2, 2, [19, 22, 43, 50])
        self.assertEqual(B_x_A, Matrices.product(B, A))

class TestAdd(unittest.TestCase):
    
    def test_add_1(self):
        A = Matrix(2, 2, [1, 1, 1, 1])
        B = Matrix(2, 2, [1, 1, 1, 1])
        self.assertEqual(Matrices.add(A, B), Matrix(2, 2, [2, 2, 2, 2]))

class TestVectorProjection(unittest.TestCase):
    
    def test_vector_projection_1(self):
        w_vector = Matrix(2, 1, [1, 0]) 
        x_vector = Matrix(2, 1, [1, 1])
        self.assertEqual(Matrices.vector_projection(w_vector, x_vector),
                Matrix(2, 1, [1, 0]))

class TestVectorReflection(unittest.TestCase):
    
    def test_vector_reflection(self):
        w_vector = Matrix(2, 1, [1, 0])
        x_vector = Matrix(2, 1, [0, 1])
        self.assertEqual(Matrices.vector_reflection(w_vector, x_vector),
            Matrix(2, 1, [0, -1]))

if __name__ == "__main__":
    unittest.main()
