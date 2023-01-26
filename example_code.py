import reduced_echelon

matrix_a = [[1,2,3],[4,5,6]]
matrix_b = [[1,0,-1],[0,1,2]]

print(reduced_echelon.reduce(matrix_a))
print(reduced_echelon.reduce(matrix_b))

if reduced_echelon.reduce(matrix_a) == reduced_echelon.reduce(matrix_b): #example of code to check row equivalence
    print("yay")
else:
    print("no")