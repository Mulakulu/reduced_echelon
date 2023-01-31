def inverse(matrix = 0):
    if matrix == 0:
        pre_defined_matrix = 0
    else:
        pre_defined_matrix = matrix
    if __name__ == "__main__":
        step_mode = 1
    else:
        step_mode = 0
    def print_matrix(printed_matrix,title = ""): #prints the matrix all nice-looking
            if title != "": print(title)
            temp_width = len(printed_matrix[0])
            temp_height = len(printed_matrix)
            clean_numbers()
            longest_string = [0]*temp_width
            for y in range(0,temp_height):
                for x in range(0,temp_width):
                    if type(printed_matrix[y][x]) == str:
                        if len(printed_matrix[y][x]) > longest_string[x]: longest_string[x] = len(printed_matrix[y][x])
                    else:
                        if len(str(round(printed_matrix[y][x],digits))) > longest_string[x]: longest_string[x] = len(str(round(printed_matrix[y][x],digits)))
            for y in range(0,temp_height):
                print("[",end="")
                for x in range(0,temp_width-1):
                    if type(printed_matrix[y][x]) == str:
                        print(f"{' '*(longest_string[x]-len(printed_matrix[y][x]))}{printed_matrix[y][x]}, ",end="")
                    else:
                        print(f"{' '*(longest_string[x]-len(str(round(printed_matrix[y][x],digits))))}{str(round(printed_matrix[y][x],digits))}, ",end="")
                if type(printed_matrix[y][temp_width-1]) == str:
                    print(f"{' '*(longest_string[temp_width-1]-len(printed_matrix[y][temp_width-1]))}{printed_matrix[y][temp_width-1]}]\n",end="")
                else:
                    print(f"{' '*(longest_string[temp_width-1]-len(str(round(printed_matrix[y][temp_width-1],digits))))}{str(round(printed_matrix[y][temp_width-1],digits))}]\n",end="")
    def clean_numbers(): #Function that cleans up -0.0's
        for y in range(0,height):
            for x in range(0,width):
                if abs(int(round(matrix[y][x]*10000))-matrix[y][x]*10000)<0.01:
                    matrix[y][x] = round(matrix[y][x]*1000)/1000
                if abs(int(round(matrix[y][x]))-matrix[y][x])<0.0000001:
                    matrix[y][x] = int(round(matrix[y][x]))
                if str(matrix[y][x]) == "-0.0": matrix[y][x] = 0
                if str(matrix[y][x]) == "0.0": matrix[y][x] = 0



    ##Options
    import sys
    import reduced_echelon as re
    digits = 3 #These do NOT change the math. Only displayed digits



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
        print_matrix(matrix,"\nMatrix shape")
        print()
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
        print_matrix(matrix,"\nMatrix input")
        print()
    else: #Runs if matrix is pre-defined
        matrix = pre_defined_matrix
        width = len(matrix[0])
        height = len(matrix)
        if step_mode == 1: print_matrix("Matrix input")
    matrix_representation = [ [0] * (width*height+1) for i in range(max(width,height)*height) ]
    for i in range(0,width): #Places the inputed matrix into big matrix representation
        for j in range(0,height):
            for k in range(0,height):
                matrix_representation[k+j*height][k+i*height] = matrix[j][i]
    if width > height:  #Define the undefined factors as 1
        for i in range(0,(width-height)*height):
            matrix_representation[-i-1][-i-2] = 1
            matrix_representation[-i-1][-1] = 1
    for i in range(0,height):
        for j in range(0,height):
            if i == j:
                matrix_representation[i*height+j][-1] = 1
    #print_matrix(matrix_representation,"Matrix representation")
    new_matrix = re.reduce(matrix_representation,True)[0]
    #print(new_matrix)
    success = 1
    for i in range(0,max(width,height)*height): #Check for 0 = 1
        is_not_zero = 0
        for j in range(0,width*height-1):
            if new_matrix[i][j] != "0": 
                is_not_zero = 1
        if is_not_zero == 0 and new_matrix[i][-2] == "1" and new_matrix[i][-1] == "0":
            success = 0
    if success == 0:
        print("There is no inverted matrix of the inputed matrix")
    else:
        output_matrix = [[0] * height for i in range(width)]
        for i in range(0,height):
            for j in range(0,width):
                output_matrix[j][i] = new_matrix[j*height+i][-1]
        print_matrix(output_matrix,"Inverse matrix")

if __name__ == "__main__":
    while True == True:
        inverse()
