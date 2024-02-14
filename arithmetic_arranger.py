def arithmetic_arranger(problem_list, answers_visible=False):
    # error_too_many = 'Too many problems.'
    # error_wrong_operand = "Operator must be '+' or '-'."
    # error_only_digits = 'Number must only contain digits.'
    # error_max_digits = 'Numbers cannot be more than four digits.'
    # if len(problems) > 5:
    #     current_error = error_too_many
    # elif '*' or '/' in problem_list:
    #     current_error = error_wrong_operand
    # elif problem_list
    #     return print(f'Error: {current_error}')
    
    # Variable Definitions
    first = True
    width_between = '    '
    line1 = line2 = line3 = line4 = ''
    split_problems = []
    #Split input
    for problem in problem_list: #Split problem_list into individual problems
        split_problems = problem.split()
        operand1 = split_problems[0] #Store first operand
        operator = split_problems[1] #Store operator
        operand2 = split_problems[2] #Store second operand
        # End separation step
        # Begin conversion to int
        operand1 = int(operand1)
        operand2 = int(operand2)
        # Create max width
        width = max(len(str(operand1)), len(str(operand2))) # Used the max func but converts to str because length only works on a string
        # Arrangement
        if first == True:
            line1 += str(operand1).rjust(width + 2)
            line2 += operator + ' ' + str(operand2).rjust(width)
            line3 += '_' * (width + 2)
            if answers_visible == True:
                if operator == '+':
                    line4 += str(operand1 + operand2)##**LEFT OFF HERE. NEED TO GET THIS TO PRINT THE ANSWER AND FORMAT IT!



    # #Assign each problem in problem_list to a variable
    # problem1 = split_problems.pop(0)
    # operand1_1 = int(problem1[0])
    # operator1 = problem1[1]
    # operand1_2 = int(problem1[2])
    # solution1 = (operand1_1 + operand1_2)
    # #prob_dict1 = {op1: problem1[0], operator1: problem1[1], op2: problem1[2]}
    # #problem1 = [problem1.split(,)]
    # problem2 = split_problems.pop(0)
    # problem3 = split_problems.pop(0)
    # problem4 = split_problems.pop(0)
    # problem5 = split_problems.pop(0)


    #for problem in split_problems:
        #operand1, operator, operand2 = split_problems.split(' ')
        #ind_list = [item.split(' ') for problem in split_problems]


    #print(split_problems)
    #print(operand1_1 + operand1_2)
    #print(solution1)
    #print(operator1)
    #print(prob_dict1)
    #print(problem_list)
    #print(operand1 + operand2)
    #print(operator)
    #print(operand2)
    #print(width)
    print(line4)
    
    
    
    
    #print(split_problems)

arithmetic_arranger(["2 + 4 "])
#arithmetic_arranger(["2 + 4 ", "8 + 16", "32 + 64", "128 + 256"])