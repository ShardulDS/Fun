import numpy as np
import prettytable as pt

def print_matrix(mat):
    temp = pt.PrettyTable(border=False, header=False)
    for k in mat:
        temp.add_row(k)
    print(temp)
    return None
matrix = [[2, 3, 5, 7], [12, 3, 9, 23], [5, 8, 15, 6], [7, 4, 18, 11]]
print_matrix(matrix)
matrix = np.array(matrix)
eigenval, eigenvecs = np.linalg.eig(matrix)
for i in range(len(eigenval)):
    print(f'''For eigen value: {np.round(eigenval[i])}
Eigen vector is:''')
    print(np.vstack(eigenvecs[:, i]))