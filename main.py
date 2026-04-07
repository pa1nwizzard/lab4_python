def repeat_calls(times, arguments):
    def decorator(func):
        def wrapper():
            results = []
            for i, arg in enumerate(arguments[:times]):
                result = func(arg)
                results.append(result)
                print(f"Вызов {i+1}: calc({arg}) = {result}")
            return results
        return wrapper
    return decorator

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

decorated_calc = repeat_calls(5, [3, 1, 2, 2, 3])(calc)
print(decorated_calc())