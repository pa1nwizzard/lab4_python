from functools import wraps

def repeat_calls(_func=None, *, times=1, arguments=None):
    if arguments is None:
        arguments = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []

            if arguments:
                for i, arg in enumerate(arguments[:times]):
                    result = func(arg)
                    print(f"Вызов {i+1}: calc({arg}) = {result}")
                    results.append(result)
            else:
                for i in range(times):
                    result = func(*args, **kwargs)
                    print(f"Вызов {i+1}: {result}")
                    results.append(result)

            return results

        return wrapper

    if _func is not None:
        return decorator(_func)

    return decorator


class RepeatCalls:
    def __init__(self, times=1, arguments=None):
        self.times = times
        self.arguments = arguments or []

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []

            if self.arguments:
                for i, arg in enumerate(self.arguments[:self.times]):
                    result = func(arg)
                    print(f"Вызов {i+1}: calc({arg}) = {result}")
                    results.append(result)
            else:
                for i in range(self.times):
                    result = func(*args, **kwargs)
                    print(f"Вызов {i+1}: {result}")
                    results.append(result)

            return results

        return wrapper


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

print("=== Декоратор-функция с параметрами ===")
calc = make_calc('+', initial=1)
decorated_calc = repeat_calls(times=5, arguments=[3, 1, 2, 2, 3])(calc)
print(decorated_calc())


print("\n=== Декоратор-функция без параметров ===")
@repeat_calls
def test(x):
    return x * 2

print(test(5))


print("\n=== Класс-декоратор ===")
calc2 = make_calc('*', initial=2)
decorated_calc2 = RepeatCalls(times=4, arguments=[2, 3, 4, 5])(calc2)
print(decorated_calc2())