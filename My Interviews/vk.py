## Напиши функцию по поиску n-числа Фибоначчи 
# (последовательность, в которой первые два числа равны 0 и 1, 
# а каждое последующее число равно сумме двух предыдущих чисел)
# (0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...)
# assert fib(0) == 0
# assert fib(5) == 5
# assert fib(9) == 34


def fib(n: 'int >= 0'):
    if n == 0 or n == 1:
        return n
    
    if n in memo:
        return memo[n]
    
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


def fib(n: 'int >= 0'):
    if n == 0:
        return n

    first = 0
    second = 1
    for _ in range(1, n):
        first, second = second, first + second

    return second
    
    
# def fib(n):
#     if n == 0:
#         return 0
#     a, b = 0, 1          
#     for i in range(1, n):
#         a, b = b, a + b  
#     return b


for i in range(9):
    print(fib(i))


def print_time(function):
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = function(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        
        return res
    
    return wrapper


"""
var arr  = ["a", "b", "c"];
switch (foo()) {
    case "print": 
        console.log(1);
        break;
    case "push":
        arr.push(5);
        break;
    default:
        console.log("NO ACTION");
}
"""


arr = ["a", "b", "c"]
result = foo()
if result == "print":
    print(1)
elif result == "push":
    arr.append(5)
else:
    print("NO ACTION")


n = 5
{"print": lambda: print(1), "push": lambda: arr.append(1)}.get(result, lambda: print('NO ACTION'))()

if result in d:
    d[result]()
else:
    print("NO ACTION")


@mid
@mid2
@mid3
def get_response(request):
    pass
    
    
# core/middleware.py
def middleware1(get_response):
    def inner(request):
        print(1)
        response = get_response(request)
        print(2)
        return response
    return inner


def middleware2(get_response):
    def inner(request):
        print(3)
        response = get_response(request)
        print(4)
        return response
    return inner


def middleware3(get_response):
    def inner(request):
        print(5)
        response = get_response(request)
        print(6)
        return response
    return inner


# settings.py
MIDDLEWARE = (
    'core.middleware.middleware1',
    'core.middleware.middleware2',
    'core.middleware.middleware3',
)
