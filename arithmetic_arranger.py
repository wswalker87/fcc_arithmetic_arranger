def exception_handler(operand1, operator, operand2):
    # Operator must be '+' or '-'. **WORKS!**
    if operator != '+' and operator != '-':
        #raise BaseException I never got these to work and need to understand why.
        return "Error: Operator must be '+' or '-'."
    # Numbers cannot be more than four digits. **WORKS!**
    if len(operand1) >= 5 or len(operand2) >= 5:
        return "Error: Numbers cannot  be more than four digits."
    # Number must only contain digits. **WORKS!**
    if not int(num1):
        return "Error: Number must only contain digits"
    if not int(num2):
        return "Error: Number must only contain digits"
    return "winnah"
    

def arithmetic_arranger(problem_list, answers_visible=False):
    # Variable Definitions
    first = True
    width_between = '    '
    line1 = line2 = line3 = line4 = ''
    global num1
    global num2
    # FCC placed a limit of 5 problems for the assignment. Check if over 5 exist.
    try:
        len(problem_list) > 5
    except:
        return "Error: Too many problems"
    # Split input
    for problem in problem_list: #Split problem_list into individual problems
        split_problems = problem.split()
        operand1 = split_problems[0] # Store first operand
        operator = split_problems[1] # Store operator
        operand2 = split_problems[2] # Store second operand
        num1 = int(operand1)
        num2 = int(operand2)
        exp = exception_handler(operand1, operator, operand2)
        if exp != "winnah":
            return(exp)
        # Create max width
        width = max(len(str(operand1)), len(str(operand2))) # Used the max func but converts to str because length only works on a string
        # First Arrangement
        if first == True:
            line1 += str(operand1).rjust(width + 2)
            line2 += operator + ' ' + str(operand2).rjust(width)
            line3 += '_' * (width + 2)
            if answers_visible == True:
                if operator == '+':
                    line4 += str(num1 + num2).rjust(width + 2)
                else:
                    line4 += str(num1 - num2).rjust(width + 2)
            first = False # Set to false to begin the loop over
        else: # Begin the rest of the problems
            line1 += str(operand1).rjust(width + 6)
            line2 += operator.rjust(5) + ' ' + str(operand2).rjust(width)
            line3 += width_between + "_" * (width + 2)
            if answers_visible == True:
                if operator == '+':
                    line4 += width_between + str(num1 + num2).rjust(width + 2)
                else:
                    line4 += width_between + str(num1 - num2).rjust(width + 2)
        if answers_visible == True:
            #return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
            print(f"{line1}\n{line2}\n{line3}\n{line4}")
        else:
            print(f"{line1}\n{line2}\n{line3}")
            #return line1 + '\n' + line2 + '\n' + line3 + '\n'



#arithmetic_arranger(["2 + 4 "])
#arithmetic_arranger(["2 + 4 ", "8 - 16"])
#arithmetic_arranger(["2 + 4 ", "8 - 16", "32 + 64"])
arithmetic_arranger(["2 + 4 ", "8 - 16", "32 + 64", "128 - 256", "512 - 102004"], True)