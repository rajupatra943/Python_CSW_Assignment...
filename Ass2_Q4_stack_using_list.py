def input_matrix(name):
    print(f"Enter elements for {name} (2x2 matrix):")
    matrix = []
    for i in range(2):
        row = []
        for j in range(2):
            val = int(input(f"{name}[{i}][{j}]: "))
            row.append(val)
        matrix.append(row)
    return matrix

# Function to display a matrix
def display_matrix(matrix, title):
    print(f"\n{title}:")
    for row in matrix:
        print("  ", row)

# Function to add two matrices
def add_matrices(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(2)] for i in range(2)]

# Function to multiply two matrices
def multiply_matrices(m1, m2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = sum(m1[i][k] * m2[k][j] for k in range(2))
    return result

# Function to sort rows based on their sum
def sort_rows_by_sum(matrix):
    return sorted(matrix, key=lambda row: sum(row))

# Main program
matrix1 = input_matrix("Matrix A")
matrix2 = input_matrix("Matrix B")

sum_matrix = add_matrices(matrix1, matrix2)
product_matrix = multiply_matrices(matrix1, matrix2)
sorted_matrix = sort_rows_by_sum(product_matrix)

# Display results
display_matrix(matrix1, "Matrix A")
display_matrix(matrix2, "Matrix B")
display_matrix(sum_matrix, "Sum of A and B")
display_matrix(product_matrix, "Product of A and B")
display_matrix(sorted_matrix, "Product Matrix Sorted by Row Sum")

