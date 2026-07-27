# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
#ask for the number of rows and columns

matrix = []
# how many matrixes are going to be used for the addition and multiplication of the matrix
matrix_count = int(input("How many matrices do you want to work with? :"))






rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
# take the number of rows and column and create the matrix column before the inputs with detailed infoof the part it is going to 
print(f"Enter the values for a {rows} x {cols} matrix:")

# take the input from the user and create the matrix, it should go through the number of rows and columns and take the input from the user and create the matrix
#it should show the row and where it is being appended to or where in the row or the column that it is being used 
def create_matrix(rows, cols):

    matrix = []
    print(f"\n--- Creating a {rows}x{cols} Matrix ---")
    for r in range(rows):
        while True:
            try:
                # Read the entire row as space-separated integers on one single line
                row_input = list(map(int, input(f"Enter row {r + 1}: ").split()))
                
                # Check if the user entered exactly the requested number of columns
                if len(row_input) != cols:
                    print(f"Error: You must enter exactly {cols} values.")
                    continue  # Restart the while loop for this row
                
                # If valid, break out of the while loop to save it
                matrix.append(row_input)
                print(f"Row {r + 1} complete: {row_input}\n")
                break
                
            except ValueError:
                print("Error: Invalid input. Please enter only integers separated by spaces.")
                
    return matrix
# --- NEW STEP: Collect all matrices in a list ---

matrices_list = []
for idx in range(matrix_count):
    print(f"\n--- Creating Matrix {idx + 1} of {matrix_count} ---")
    new_matrix = create_matrix(rows, cols)
    matrices_list.append(new_matrix)

# Print all collected matrices to show the user
for idx, mat in enumerate(matrices_list):
    print(f"\nMatrix {idx + 1}:")
    for row in mat:
        print(" ".join(f"{val:<4}" for val in row))


# Part A — Transpose a Matrix
#compute for the transpose of the matrix

def transpose_matrix(a):
    transposed = []
    for j in range(len(a[0])):
        new_row = []
        for i in range(len(a)):
            new_row.append(a[i][j])
        transposed.append(new_row)
    return transposed

# Display the transposed matrix
print("Transposed Matrix:")
for row in transpose_matrix(matrices_list[0]):
    print(" ".join(f"{val:<4}" for val in row))


# Part B — Add Two Matrices
def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Error: Matrices must be of the same size to add.")
        return None

    result = []
    for i in range(len(a)):
        new_row = []

        for j in range(len(a[0])):
            new_row.append(a[i][j] + b[i][j])
        result.append(new_row)

    return result

# Display the sum of the two matrices
print("Sum of Matrices:")
for row in add_matrices(matrices_list[0], matrices_list[1]):
    print(" ".join(f"{val:<4}" for val in row))


# part C — Multiply Two Matrices
def multiply_matrices(a, b):
    # if len(a[0]) != len(b):
    #     print("Error: Number of columns in A must equal number of rows in B for multiplication.")
    #     return None

    result = []
    for i in range(len(a)):
        new_row = []
        for j in range(len(b[0])):
            sum_product = 0
            for k in range(len(b)):
                sum_product += a[i][k] * b[k][j]
            new_row.append(sum_product)
        result.append(new_row)

    return result

# Display the product of the two matrices
print("Product of Matrices:")
for row in multiply_matrices(matrices_list[0], matrices_list[1]):
    print(" ".join(f"{val:<4}" for val in row))