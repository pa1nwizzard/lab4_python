def make_calc(op, initial=0):
    count = 0
    result = initial
    
    def calc(x):
        nonlocal count, result
        
        if count >= 4:

            return result
        
        match op:
            case '+':
                result += x
            case '-':
                result -= x
            case '*':
                result *= x
            case '/':
                result /= x
            case _:
                return 0
        
        count += 1
        return result
        
    return calc

calc = make_calc('+', initial=1)
print(calc(3))
print(calc(2))
print(calc(2))
print(calc(2))
print(calc(2))
print(calc(2))