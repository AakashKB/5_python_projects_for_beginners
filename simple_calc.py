#Checks if a given string is a floating point number
def is_number(term):
    try:
        float(term)
    #If you try to cast a non-float string into a float, it throws a ValueError
    except ValueError:
        #If we get a ValueError here, we know the string is not a float
        return False
    return True

#Checks the user's input to see if it is a proper expression
def is_expression_valid(expression):
    #All expressions have a minimum of 3 terms, and have an odd number of terms
    if len(expression) < 3 or len(expression) % 2 == 0: return False

    # a list of valid non-number chars for our expression
    valid_chars = ['+', '-', '*', '/']
    
    is_prev_term_number = False
    for term in expression:
        if not term in valid_chars:
            #Returns false if term is not a number or there were two numbers in a row
            return is_number(term) and not is_prev_term_number
        else:
            #Returns false if there are two terms in a row
            if not is_prev_term_number:
                    return False
            is_prev_term_number = False

    return is_prev_term_number

#Computes all multiplication and division in the expression
def compute_mult_div(expression):
    new_expression = [expression[0]]
    prev_num = float(expression[0])

    #Loop through all terms starting from the 2nd
    for i in range(1, len(expression)):
        term = expression[i]
        prev_term = expression[i-1]

        #If current term is number, apply the operation from the previous term
        if is_number(term):
            if prev_term == "*":
               prev_num *= float(term)
               new_expression[-1] = prev_num
            elif prev_term == "/":
                prev_num /= float(term)
                new_expression[-1] = prev_num
            else:
                prev_num = float(term)
                new_expression.append(term)
        elif term == "+" or term == "-":
            new_expression.append(term)
    return new_expression

#Computer all addition and subtraction in the expression
def compute_add_sub(expression):
    prev_num = float(expression[0])
    #Loop through all items starting from the second
    for i in range(1, len(expression)):
        term = expression[i]
        prev_term = expression[i-1]
        #If term is a number, apply the operation from the previous term
        if is_number(term):
            if prev_term == "+":
                prev_num += float(term)
            elif prev_term == "-":
                prev_num -= float(term)
    return prev_num

print("Welcome to the Simple Calculator")
#Infinite loop to keep calculator running
while True:
    print("_______________________________________________________")
    print("Available operations are '+', '-', '*', and '/'")
    expression = input("Enter an expression > ").split(' ')

    #Print error if expression is invalid
    if not is_expression_valid(expression):
        print("Please enter a valid expression using the available operations")
        break

    #Compute mult/div first then computer add/sub after
    #We do it this way because of PEMDAS
    answer = compute_add_sub(compute_mult_div(expression))

    #Print answer using formatted string
    print(f'Answer: {answer}')
