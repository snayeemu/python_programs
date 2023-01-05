def fib(number, memo):
    if memo[number] is not None:
        return memo[number]
    if number <= 2:
        result = 1
    else:
        result = fib((number - 1), memo) + fib((number - 2), memo)
    memo[number] = result
    return result


number = 7
memo = [None] * (number + 1)
print(fib(number, memo))
