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
    def clean_numbers(): #Function that cleans up -0.0's
        for y in range(0,height):
            for x in range(0,width):
                if abs(int(round(matrix[y][x]*10000))-matrix[y][x]*10000)<0.01:
                    matrix[y][x] = round(matrix[y][x]*1000)/1000
                if abs(int(round(matrix[y][x]))-matrix[y][x])<0.0000001:
                    matrix[y][x] = int(round(matrix[y][x]))
                if str(matrix[y][x]) == "-0.0": matrix[y][x] = 0
                if str(matrix[y][x]) == "0.0": matrix[y][x] = 0
    def matrix_multiplication(matrix1,matrix2):
        if len(matrix2) == len(matrix1[0]):
            pass
        else:
            if len(matrix1) == len(matrix2[0]):
                temp_matrix = matrix1
                matrix1 = matrix2
                matrix2 = temp_matrix
            else: return 0
        new_matrix = [ [0] * len(matrix2[0]) for i in range(len(matrix1)) ]
        for i in range(0,len(new_matrix)):
            for j in range(0,len(new_matrix[0])):
                sum = 0
                for k in range(0,len(matrix2)):
                    sum += matrix1[i][k]*matrix2[k][j]
                new_matrix[i][j] = try_int(sum)
        return new_matrix

    ##Options
    import sys
    try: 
        import reduced_echelon as re
    except ImportError: 
        print("reduced_echelon.py was not able to be imported")
        wait = input("")
        sys.exit()

    digits = 3 #These do NOT change the math. Only displayed digits

    #matrix1 = [[1,0],[0,1]]
    #matrix2 = [[1,0],[0,1]]
    #print(matrix_multiplication(matrix1,matrix2))

    if pre_defined_matrix == 0 and step_mode == 1: #Define variables and matrix
        print()
        success = 0
        while success == 0:
            success = 1
            try:
                width = int(input("How wide is the matrix?: "))    
                if width == 0:
                    width = int("meh")
                height = int(input("How tall is the matrix?: "))
                if height == 0:
                    height = int("meh")
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
        print(f"The elements in rows past row {height} are variables that has been defined as 1. \nThis is not a unique answer.\n")
    for i in range(0,height):
        for j in range(0,height):
            if i == j:
                matrix_representation[i*height+j][-1] = 1

    new_matrix = re.reduce(matrix_representation,True)[0]

    new_float_matrix = re.reduce(matrix_representation,False)

    output_matrix = [[0] * height for i in range(width)]
    for i in range(0,height):
        for j in range(0,width):
            output_matrix[j][i] = new_matrix[j*height+i][-1]
    
    output_float_matrix = [[0] * height for i in range(width)]
    for i in range(0,height):
        for j in range(0,width):
            output_float_matrix[j][i] = try_int(new_float_matrix[j*height+i][-1])

    #Generate itentity matrix
    identity = [ [0] * height for i in range(height)]
    for i in range(0,height):
        identity[i][i] = 1

    if matrix_multiplication(matrix,output_float_matrix) == identity:
        print_matrix(output_matrix,"Inverse matrix")
    else:
        print("The program was unable to find an inverse")

if __name__ == "__main__":
    while True == True:
        inverse()
