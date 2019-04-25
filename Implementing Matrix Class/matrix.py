import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1 and self.w == 1:
            return self.g[0][0]
        
        a = self.g[0][0]
        b = self.g[0][1]
        c = self.g[1][0]
        d = self.g[1][1]
        
        return (a*d - b*c)  

    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        total = 0
        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    total += self.g[i][j]
        return total
    
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inverse = []
        
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.h == 1 and self.w == 1:
            inverse = [ [1/self.g[0][0]] ]
    
        # If the matrix is 2x2, check that the matrix is invertible
        if self.h == 2 and self.w == 2:
            det = self.determinant()
            if det == 0:
                raise RuntimeError('The matrix don\'t have inverse')
            else:
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]
                factor = 1/det
                inverse = [[d, -b],[-c, a]]
            
                for i in range(len(inverse)):
                    for j in range(len(inverse[0])):
                        inverse[i][j] = factor * inverse[i][j]

        return Matrix(inverse)
    
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for row in range(self.w):
            new_row = []
            for col in range(self.h):
                new_row.append(self.g[col][row])
            matrix_transpose.append(new_row)
        return Matrix(matrix_transpose)
    

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSum = []
    
        # matrix to hold a row for appending sums of each element
        row = []

        for i in range(self.h):
            row = []
            for j in range(self.w):
                new_val = self.g[i][j] + other[i][j]
                row.append(new_val)
            matrixSum.append(row)

        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        neg_mat = []
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-self.g[i][j])
            neg_mat.append(row)
            
        return Matrix(neg_mat)
    

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be substracted if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSub = []
    
        # matrix to hold a row for appending sums of each element
        row = []

        for i in range(self.h):
            row = []
            for j in range(self.w):
                new_val = self.g[i][j] - other[i][j]
                row.append(new_val)
            matrixSub.append(row)

        return Matrix(matrixSub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        if self.w != other.h:
            raise(ValueError, "Number of rows of 1st matrix and the "+ 
                              "#height of the other must be equal for Matrix Multiplication.")
        
        
        def get_row(matrix, row):
            return matrix[row]
        
        def get_column(matrix, column_number):
            column = []
            for row in range(matrix.h):
                column.append(matrix[row][column_number])
            return column

        def dot_product(vector_one, vector_two):
            summ = 0
            for i in range(len(vector_one)):
                summ += vector_one[i]*vector_two[i]
            return summ
        
        result = []
        
        for i in range(self.h):
            row_result = []
            for j in range(other.w):
                row = get_row(self.g, i)
                col = get_column(other, j)
                row_result.append(dot_product(row, col))
            result.append(row_result)
        return Matrix(result)
        
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        r = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                new_val = other * self.g[i][j]
                row.append(new_val)
            r.append(row)
        return Matrix(r)
        
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            