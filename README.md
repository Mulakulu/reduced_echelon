# Use program as is
You can open reduce_echelon.py as is and input the matrix you want to reduce. It spits out the solving steps required to reduce it and at the end, it calculates the fractional representation of decimal numbers. This can take some time based on the complexity of the calculation. Usually, if the program isn't done computing it in a reasonable time, the fractions won't be reasonable anyway.

In the py file, there is a variable named "digits" where you can change the amount of digits show. Default is 3.
Digits shown does not change any of the math.


# Import program to another program
You can use the program externally for simplifying matrixes, just by importing it and writig something like:

import reduced_echelon

new_matrix = reduced_echelon.reduce(old_matrix)

The above code will return the reduced form of the matrix in decimal form. It skips the fraction calculation for speed and simplicity. 
Some other uses for this function would be to see if two rows are row equivalent

if reduced_echelon.reduce(matrix_a) == reduced_echelon.reduce(matrix_b):

See example_echelon.py for an example

# Future plans
I will let imported reduce() give fractions if requested, so "reduce(matrix)" will give decimal while "reduce(matrix,True)" will return fractions. The output will return the fractions as a string of the fraction with the numerator and denominator, so your code needs to check for strings
an example of how an output might look would be:
[[1,0.5],[1,1]] returning [[1,"1/2"],[1,1]]
I'm aware it should have been a list, but I coded it with strings initally and changing it would be bothersome.
