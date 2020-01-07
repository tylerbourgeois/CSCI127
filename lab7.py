# --------------------------------------
# CSCI 127, Lab 7
# October 17, 2017
# Tyler Bourgeois
# --------------------------------------
def print_matrix(matrix, rows, columns, name):
    print(name)
    print()
    print_header(columns)
    for i in range(rows):
        print("|", end="")
        for j in range(columns):
            value = "  " + str(matrix.get((i,j)))
            if(value == ("  " + str(None))): value = "  " + str(0)
            if(int(value) < 0): value = " " + str(int(value))
            print(str(value) + "|", end="")
            if(matrix.get((i,j)) == 0): matrix.delete((i,j)) 
        print()
        print_header(columns)
    print()
    
def add_matrices(matrix_1, matrix_2, rows, columns):
    new_matrix = {}
    for i in range(rows):
        for j in range(columns):
            matrix_1_value = matrix_1.get((i,j))
            matrix_2_value = matrix_2.get((i,j))
            if(matrix_1_value == None): matrix_1_value = 0
            if(matrix_2_value == None): matrix_2_value = 0
            if((matrix_1_value + matrix_2_value) != 0):
                new_matrix[(i,j)] = matrix_1_value + matrix_2_value
    return new_matrix

# --------------------------------------
# Do not change anything below this line
# --------------------------------------

def print_header(columns):
    line = "+"
    for i in range(columns):
        line += "---+"
    print(line)

# --------------------------------------

def read_matrix(input_file):
    matrix = {}
    line = input_file.readline().split()
    while line[0] != "stop":
        row = int(line[0])
        column = int(line[1])
        value = int(line[2])
        matrix[(row, column)] = value
        line = input_file.readline().split()
    return matrix

# --------------------------------------

def main (file_name):
    input_file = open(file_name, "r")
    
    line = input_file.readline().split()
    rows = int(line[0])
    columns = int(line[1])

    matrix_1 = read_matrix(input_file)
    print_matrix(matrix_1, rows, columns, "Matrix 1")
    
    matrix_2 = read_matrix(input_file)
    print_matrix(matrix_2, rows, columns, "Matrix 2")

    matrix_3 = add_matrices(matrix_1, matrix_2, rows, columns)
    print_matrix(matrix_3, rows, columns, "Matrix 1 + Matrix 2")
    print("Matrix 3 =", matrix_3)

# --------------------------------------

main ("sparse-matrix.txt")
