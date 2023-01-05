from Stack import Stack


def postfix_evaluation(given_expression):
    numbers = "0123456789"
    token_list = given_expression.split()
    stack = Stack()
    for token in token_list:
        if token in numbers:
            stack.push(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = do_math(token, int(operand1), int(operand2))
            stack.push(result)
    return stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "/":
        return op1 / op2


print(postfix_evaluation("1 2 +"))
