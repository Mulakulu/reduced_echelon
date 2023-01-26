# Use reduce_echelon.py
You can open reduce_echelon.py as is and input the matrix you want to reduce. It spits out the solving steps required to reduce it and at the end, it calculates the fractional representation of decimal numbers. This can take some time based on the complexity of the calculation. Usually, if the program isn't done computing it in a reasonable time, the fractions won't be reasonable anyway.

In the py file, there is a variable named "digits" where you can change the amount of digits show. Default is 3.
Digits shown does not change any of the math.

# Use find_inverse_matrix.py
You can open find_inverse_matrix.py as is so long as you have reduce_echelon.py in the same folder. When opened, it asks for the matrix you want to invert and it is as simple as that. For square matrixes, it will return the unique inverted matrix if there is one, for m>n matrixes, it returns one of infinite valid inverted matrixes where it defined undefined variables as 1 and for n>m matrixes, it will try to find a unique inverted matrix, although I don't believe there are any.


# Import reduce_echelon to another program
You can use the program externally for simplifying matrixes, just by importing it and writig something like:

import reduced_echelon

new_matrix = reduced_echelon.reduce(old_matrix)

The above code will return the reduced form of the matrix in decimal form. It skips the fraction calculation for speed and simplicity. 
Some other uses for this function would be to see if two rows are row equivalent

if reduced_echelon.reduce(matrix_a) == reduced_echelon.reduce(matrix_b):

See example_echelon.py for an example

# Future plans
making find_inverted_matrix into an importable package
making a standalone version of find_inverted_matrix
