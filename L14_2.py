# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)

def is_identity_matrix(matrix):
    #Write your code here

    if matrix == []:
        return False
    else:
        # check whether it is a square matrix
        for i in matrix:
            if len(i) != len(matrix):
                return False
            else:
                col = 0
                while col <= len(matrix)-1:
                    row = 0
                    while row <= len(matrix)-1:
                        # print(matrix[row][col])
                        if row == col:
                            if matrix[row][col] == 1:
                                marker = True
                            else:
                                return False
                        else:
                            if matrix[row][col] == 0:
                                marker = True
                            else:
                                return False
                        row = row + 1
                    col = col + 1
    return marker



# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print(is_identity_matrix(matrix1))
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print(is_identity_matrix(matrix2))
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print(is_identity_matrix(matrix3))
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print(is_identity_matrix(matrix4))
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print(is_identity_matrix(matrix5))
#>>>False

matrix6 = [[1,0,0,0],
           [0,1,0,1],
           [0,0,1,0],
           [0,0,0,1]]

print(is_identity_matrix(matrix6))
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print(is_identity_matrix(matrix7))
#>>>False
