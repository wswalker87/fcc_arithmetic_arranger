def arithmetic_arranger(problem_list):
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
    
    #Split input

    split_problems = []
    # operand1 = None
    # operator = None
    # operand2 = None
    for problem in problem_list:
        operand1, operator, operand2 = problem.split()
    # #prob_dict1 = {}
    # for input in problem_list:
    #     #split into a list of comma sep lists
    #     split_problems = [problem.split() for problem in problem_list]
    # #for problem in split_problems:
    #     #operand1, operator, operand2 = split_problems[:].split()


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
    print(operand1)
    
      
    
    
    
    #print(split_problems)


arithmetic_arranger(["2 + 4 ", "8 + 16", "32 + 64", "128 + 256", "null"])