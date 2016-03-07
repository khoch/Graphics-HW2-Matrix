import math
#testm1 = [[1, 2, 3], [4, 5, 6]]
#testm2 = [[7, 8], [9, 10], [11, 12]]

def print_matrix(matrix):
    mymat = "\n"
    for r in matrix:
        mymat += "| "
        for e in r:
            mymat += str(e) + " | "
        mymat += "\n"
    print mymat

def can_multiply(m1, m2):
    return (len(m1[0]) == len(m2))
	
def scalar_multiply(matrix, scale):
    newmat = []
    for r in matrix:
        temprow = []
        for e in r:
            temprow.append(scale * e)
        newmat.append(temprow)
    return newmat

def matrix_multiply(m1, m2):
    newmat = []
    for r in m1:
        temprow = []
        for c in range(len(m2[0])): #for each column in m2:
            tempelem = 0
            for e in range(len(m1[0])): #for each element in the current row,
                tempelem += r[e] * m2[e][c] #multiply it by the corresponding element in the current column of m2
            temprow.append(int(tempelem))
        newmat.append(temprow)
    return newmat

def create_identity(row=4, col=4):
    newmat = []
    for r in range(row):
        temprow = []
        for c in range(col):
            if (c == r):
                temprow.append(1)
            else:
                temprow.append(0)
        newmat.append(temprow)
    return newmat

def create_scale(x, y, z):
    newmat = []
    for r in range(4):
        temprow = []
        for c in range(4):
            temprow.append(0)
        newmat.append(temprow)
    newmat[0][0] = x
    newmat[1][1] = y
    newmat[2][2] = z
    newmat[3][3] = 1
    return newmat
	
def create_translation(x, y, z):
    newmat = create_identity(4, 4)
    newmat[3][0] = x
    newmat[3][1] = y
    newmat[3][2] = z
    return newmat

def create_rotate_x(theta):
    newmat = create_identity(4, 4)
    newmat[2][2] = math.cos(math.radians(theta))
    newmat[1][1] = math.cos(math.radians(theta))
    newmat[2][1] = math.sin(math.radians(theta))
    newmat[1][2] = math.sin(math.radians(theta))*-1
    return newmat
	
def create_rotate_y(theta):
    newmat = create_identity(4, 4)
    newmat[0][0] = math.cos(math.radians(theta))
    newmat[2][2] = math.cos(math.radians(theta))
    newmat[0][2] = math.sin(math.radians(theta))*-1
    newmat[2][0] = math.sin(math.radians(theta))
    return newmat
	
def create_rotate_z(theta):
    newmat = create_identity(4, 4)
    newmat[0][0] = math.cos(math.radians(theta))
    newmat[1][1] = math.cos(math.radians(theta))
    newmat[1][0] = math.sin(math.radians(theta))
    newmat[0][1] = math.sin(math.radians(theta))*-1
    return newmat

#print_matrix(testm1)
#print_matrix(scalar_multiply(testm1, 2))

#if can_multiply(testm1, testm2):
#    print_matrix(matrix_multiply(testm1, testm2))
#print_matrix(create_identity(4, 4))