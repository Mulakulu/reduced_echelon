def reduce(matrix = 0):
    if matrix == 0:
        pre_defined_matrix = 0
    else:
        pre_defined_matrix = matrix
    if __name__ == "__main__":
        step_mode = 1
    else:
        step_mode = 0
    def switch_two_rows(row1,row2): #Function that swaps two rows
        temp_row = matrix[row1]
        matrix[row1] = matrix[row2]
        matrix[row2] = temp_row
        if dev_mode == 1: 
            print_matrix(f"switch_two_rows(row1: {row1}, row2: {row2})")
        elif step_mode == 1:
            print_matrix(f"switch row {row1+1} and row {row2+1}")
    def multiply_row_by_factor(row,factor): #Function that multiplies a row by a factor
        if factor != 1:
            factor = try_int(factor)
            for i in range(0,width):
                matrix[row][i] = matrix[row][i] * factor
            multiply_multiplier(factor)
            if dev_mode == 1:
                print_matrix(f"multiply_row_by_factor(row: {row}, factor: {round(factor,digits)})")
            elif step_mode == 1 and factor != 1:
                print_matrix(f"Multiply row {row + 1} by {round(factor,digits)}")
    def add_multiple_of_row(row1,row2,factor): #Function that multiplies row1 by factor and adds it to row 2
        if factor != 0:
            for i in range(0,width):
                matrix[row2][i] = matrix[row2][i] + matrix[row1][i]*factor
            multiply_multiplier(factor)
            if dev_mode == 1:
                print_matrix(f"add_multiple_of_row(row1 = {row1}, row2 = {row2}, factor = {round(factor,digits)})")
            elif step_mode == 1:
                print_matrix(f"Add row {row1+1} multiplied by {round(factor,digits)} to row {row2+1}")
    def index_of_leading_digits(): #Returns a list of the index of the leading digets
        index = []
        for y in range(0,height):
            index.append(width)
            x = 0
            if check_entire_zero_row(y) == 0:
                while(index[y] == width):
                    if matrix[y][x] != 0: 
                        index[y] = x
                    x += 1
        return index
    def sort_rows(): #Function that sorts the rows so they attempt to follow rule 2
        for i in range(0,height-1):
            list_of_indexes = index_of_leading_digits()
            for y in range(0,height-1):
                if list_of_indexes[y] > list_of_indexes[y+1]: switch_two_rows(y,y+1)
    def check_entire_zero_row(row): #Returns 1 if the row is entirely 0's or 0 if it isn't
        succeed = 1
        for x in range(0,width):
            if matrix[row][x] != 0: succeed = 0
        return succeed
    def print_matrix(title = ""): #prints the matrix all nice-looking
        if title != "": print(title)
        clean_numbers()
        longest_string = [0]*width
        for y in range(0,height):
            for x in range(0,width):
                if len(str(round(matrix[y][x],digits))) > longest_string[x]: longest_string[x] = len(str(round(matrix[y][x],digits)))
        for y in range(0,height):
            print("[",end="")
            for x in range(0,width-1):
                print(f"{' '*(longest_string[x]-len(str(round(matrix[y][x],digits))))}{str(round(matrix[y][x],digits))}, ",end="")
            print(f"{' '*(longest_string[width-1]-len(str(round(matrix[y][width-1],digits))))}{str(round(matrix[y][width-1],digits))}]\n",end="")
        print()
    def remove_variable(row1,row_change): #Function that uses add_multiple_of_row to shorten row_change
        indexes = index_of_leading_digits()
        add_multiple_of_row(row1,row_change,-matrix[row_change][indexes[row_change]]/matrix[row1][indexes[row1]])
        multiply_multiplier(matrix[row_change][indexes[row_change]])
        multiply_multiplier(matrix[row1][indexes[row1]])
    def find_equally_long_rows_and_fix(): #Function that finds equally long rows and eliminates them
        for i in range(0,height-1):
            for j in range(0,height-1-i):
                indexes = index_of_leading_digits()
                j_inv = height-j-1
                if indexes[i] == indexes[j_inv] and indexes[i] != width:
                    turn_leading_digit_one(i)
                    remove_variable(i,j_inv)
        for y in range(0,height):
            turn_leading_digit_one(y)
        clean_numbers()
    def turn_leading_digit_one(row): #Function that turns the leading digit to 1. Assumes it's not fead a 0's row
        indexes = index_of_leading_digits()
        if indexes[row] != width: multiply_row_by_factor(row,1/matrix[row][indexes[row]])
    def clean_numbers(): #Function that cleans up -0.0's
        for y in range(0,height):
            for x in range(0,width):
                if abs(int(round(matrix[y][x]*10000))-matrix[y][x]*10000)<0.01:
                    matrix[y][x] = round(matrix[y][x]*1000)/1000
                if abs(int(round(matrix[y][x]))-matrix[y][x])<0.0000001:
                    matrix[y][x] = int(round(matrix[y][x]))
                if str(matrix[y][x]) == "-0.0": matrix[y][x] = 0
                if str(matrix[y][x]) == "0.0": matrix[y][x] = 0
    def reduced_row_based(): #Hopefully a function that turns an Echelon form to a reduced Echelon from
        sort_rows()
        indexes = index_of_leading_digits()
        for y in range(1,height):
            for yy in range(0,y):
                if indexes[y] != width: 
                    add_multiple_of_row(y,yy,-(matrix[yy][indexes[y]])/(matrix[y][indexes[y]]))
                    multiply_multiplier(matrix[yy][indexes[y]])
                    multiply_multiplier(matrix[y][indexes[y]])
                indexes = index_of_leading_digits()
        clean_numbers()
    def simplify_fraction(numerator,denominator):
        numerator = try_int(numerator)
        denominator = try_int(denominator)
        while is_whole(numerator) == False:
            i = 1
            success = 0
            while success == 0:
                if is_whole(numerator * i) == True:
                    numerator = try_int(numerator*i)
                    denominator  = try_int(denominator*i)
                    success = 1
                else:
                    i += 1
        i = 2
        success = 0
        while success == 0:
            if i > denominator:
                success = 1
            else:
                if is_whole(numerator/i) == True and is_whole(denominator/i) == True :
                    numerator = try_int(numerator/i)
                    denominator = try_int(denominator/i)
                    i = 2
                else:
                    i += 1
        fraction = [try_int(numerator),try_int(denominator)]
        return fraction
    def fractionify(): #Turns numbers for the output into their simplest fractions
        for y in range(0,height):
            for x in range(0,width):
                if is_whole(matrix[y][x]) == False:
                    fraction = simplify_fraction(matrix[y][x]*multiplier_simplified,multiplier_simplified)
                    if fraction[1] == 1:
                        nice_matrix[y][x] = f"{fraction[0]}"
                    else:
                        nice_matrix[y][x] = f"{fraction[0]}/{fraction[1]}"
                else:
                    nice_matrix[y][x] = str(round(matrix[y][x],2))
    def try_int(num): #Turns numbers like 4.0 to 4
        if is_whole(num):
            return int(round(num))
        else:
            if abs(int(round(num*10000))-num*10000)<0.01:
                num = round(num*10000)/10000
            return num
    def is_whole(num): #Tests if a float is close enough to a whole number to count as one
        if abs(int(round(num))-num) < 0.0000001:
            return True
        else:
            return False
    def print_nice_matrix(): #Printing the output with factors and everything
        fractionify()
        print("Output matrix in fractions")
        longest_string = [0]*width
        for y in range(0,height):
            for x in range(0,width):
                if len(nice_matrix[y][x]) > longest_string[x]: longest_string[x] = len(nice_matrix[y][x])
        for y in range(0,height):
            print("[",end="")
            for x in range(0,width-1):
                print(f"{' '*(longest_string[x]-len(nice_matrix[y][x]))}{nice_matrix[y][x]}, ",end="")
            print(f"{' '*(longest_string[width-1]-len(nice_matrix[y][width-1]))}{nice_matrix[y][width-1]}]\n",end="")
    def multiply_multiplier(factor): #Updating the multiplier that's used in the final fractionify function
        if factor != 0:
            factor = max([abs(factor),abs(1/factor)])
            factor = try_to_make_whole(factor)
            if factor not in multiplier: multiplier.append(factor)
            if dev_mode == 1: print(f"Multiplier {str(multiplier)}\n")
    def try_to_make_whole(num): 
        success = 0
        i = 1
        while success == 0:
            try_num = num
            if is_whole(try_num * i):
                success = 1
                return try_int(num * i)
            else:
                i += 1


                                                                          
    ##Options
    import sys
    dev_mode = 0 #Gives even more information. Useless for someone who just wants to use the tool
    digits = 3 #These do NOT change the math. Only displayed digits



    #Generating the matrix
    if pre_defined_matrix == 0 and step_mode == 1: #Define variables and matrix
        print()
        success = 0
        while success == 0:
            success = 1
            try:
                width = int(input("How wide is the matrix?: "))    
                height = int(input("How tall is the matrix?: "))
            except ValueError:
                print("Invalid input. Try again")
                success = 0
            except KeyboardInterrupt:
                sys.exit()
        matrix = [ [0] * width for i in range(height) ]
        print_matrix("\nMatrix shape")
        multiplier_simplified = 1
        nice_matrix = [ [0] * width for i in range(height) ]
        multiplier = [1]
        for y in range(0,height):
            for x in range(0,width):
                success = 0
                while success == 0:
                    success = 1
                    try:
                        matrix[y][x] = float(input(f"Row {y+1} Column {x+1}: "))
                    except ValueError:
                        print("Invalid input. Try again")
                        success = 0
                    except KeyboardInterrupt:
                        sys.exit()
        print()
        print_matrix("Matrix input")
    else: #Runs if matrix is pre-defined
        matrix = pre_defined_matrix
        width = len(matrix[0])
        height = len(matrix)
        multiplier_simplified = 1
        nice_matrix = [ [0] * width for i in range(height) ]
        multiplier = [1]
        if step_mode == 1: print_matrix("Matrix input")
    succeed = 1
    while succeed == 1: #Solver
        old_matrix = str(matrix)
        succeed = 0
        clean_numbers()
        sort_rows()
        find_equally_long_rows_and_fix()
        sort_rows()
        if old_matrix != str(matrix): succeed = 1
    reduced_row_based()
    for i in range(0,len(multiplier)):
        multiplier_simplified *= multiplier[i]
    if dev_mode == 1: print(f"Final factors for simplifying {multiplier_simplified}\n")
    if step_mode == 1: 
        fractionify()
        print_nice_matrix()
    return matrix

if __name__ == "__main__":
    while True == True:
        reduce()