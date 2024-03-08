from math import sqrt
from operator import (
    add,
    sub,
    mul,
)

import threading

"""Module corresponding to the linear algebra functions that `evaluate` in
src.interpreter.interpreter uses."""

class Number:

    def __add__(self, other):
        
        return self.add(other)

    def __sub__(self, other):

        return self.sub(other)

    def __mul__(self, other):

        return self.mul(other)

class Vector(Number):
    
    def add(self, other):
        """ 
        Vector Vector -> Vector

        given two Vectors 'add' adds them together.

        given: Vector([2,3,5]) + Vector([4,5,6])

        expect: Vector([6,8,11])
        """

        if isinstance(other, Vector):

            return [s + t for s, t in zip(self.contents, other.contents)]
        
        else:
            raise ValueError("{} is not type Vector.".format(other))

    def sub(self, other):
        """
        Vector Vector -> Vector

        given two Vectors 'sub' substracts them.

        given: Vector([2,3,5]) Vector([4,6,7])

        expect: Vector([-2,-3,-2])
        """

        if isinstance(other, Vector):

            return [s - t for s, t in zip(self.contents, other.contents)]
        
        else:
            raise ValueError("{} is not type Vector.".format(other))

    def mul(self, other):
        """
        Vector Vector -> Scalar or Vector Scalar -> Vector

        computes the DOT-PRODUCT of the two given Vectors if other is of type VECTOR;
        otherwise, if other is of type INT, it multiplies Vector by a scalar.

        given: Vector([-6, 8]) * Vector([5, 12])
        expect: 66 

        given: Vector([2,3,4,5]) * 3
        expect: [6,9,12,15]
        """
        

        if isinstance(other, Vector):
            
            return sum([t * u for t, u in zip(self.contents, other.contents)])

        elif isinstance(other, int):

            return [other * t for t in self.contents]

        else:
            raise ValueError("{} is not of type VECTOR or INT.".format(other))

class M(Number):

    def add(self, other):
        """
        M M -> M

        returns the SUM of the two given matrices.

        given: M([[2,3,5], [5,6,7]]) + M([[3,4,5], [5,6,7]])

        expect: [[5,7,10], [10,12,14]]
        """
        if isinstance(other, M):
            
            return [list(map(add,t,u)) for t, u in zip(self.contents, other.contents)]
        
        else:
            
            raise ValueError("{} is not of type M.".format(other))

    def sub(self, other):
        """
        M M -> M

        returns the DIFFERENCE of the given two matrices.

        given: M([[4,5,6], [5,6,7]]) - M([[2,3,4], [2,3,4]])

        expect: [[2,2,2], [3,3,3]]
        """
        if isinstance(other, M):

            return [list(map(sub, t, u)) for t, u in zip(self.contents, other.contents)]

        else:

            raise ValueError("{} is not of type M.".format(other))

    def mul(self, other):
        """
        M M -> M or M Scalar -> M

        returns the product of two matrices if the type of other is M; otherwise 
        if  the type of other is INT then it returns the matrix multplied by a scalar.

        given: M([[1,2,3], [4,5,6]]) * M([[7,8], [9,10], [11,12]])

        expect: [[58,64], [139, 154]]

        given: M([[2,3,4], [3,4,5]) * 4

        expect: [[8,12,16], [12,16,20]]
        """

        if isinstance(other, M):

            if len(self.contents) == len(self.contents[0]) and len(other.contents[0]) == len(other.contents):
                m3 = [[0 for _ in range(len(self.contents))] for _ in range(len(self.contents))]
                r = None
                for k in range(len(self.contents)):
                    for i in range(len(self.contents)):
                        r = self.contents[i][k]
                        for j in range(len(self.contents)):
                            m3[i][j] += r * other.contents[k][j]
                return m3
            else:
                return [compute_ith_vector(self.contents, other.contents, i) for i in range(len(self.contents))]

        elif isinstance(other, int):

            return [[other * i for i in x] for x in self.contents]

        else:

            raise ValueError("{} is not of type M.".format(other))
       
class V(Vector):

    def __init__(self, contents):
        self.contents = contents

    def magnitude(self):
        """
        Vec -> Scalar

        given a Vec 'magnitude' returns the magnitude.

        given: Vec([6,8])

        expect: 10
        """

        return sqrt(sum([x * x for x in self.contents]))

    def is_unit_vector(self):

        """
        Vector -> Bool 

        check if the Vector is a UNIT-VECTOR.

        given: Vec([6,8])

        expect: False

        given: Vec([1,0,0])

        expect: True 
        """

        return self.magnitude() == 1

class Mat(M):

    def __init__(self, contents):
        self.contents = contents

    def transpose(self):

        return [get_first(self.contents, i) for i in range(len(self.contents[0]))]
    

def compute_ith_vector(m, m2, i):

    return [sum([a * b for a, b in zip(m[i], get_column(m2, j))])
            for j in range(len(m2[0]))]
        
 
def get_column(m, index):
    c = []
    for k in range(len(m)):
        c.append(m[k][index])

    return c

def get_first(m, index):
    firsts = []
    for i in range(len(m)):
        firsts.append(m[i][index])
            
    return firsts

def parallel_sq_matrix_mul(mat1, mat2):
    def multiply(row, a, b, result):
        for i in range(len(b[0])):
            for j in range(len(b)):
                result[row][i] += a[row][j] * b[j][i]

    m3 = [[0 for _ in range(len(mat1))] for _ in range(len(mat1))]

    threads = []
    for i in range(len(mat1)):
        thread = threading.Thread(target=multiply, args=(i, mat1, mat2, m3))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return m3
