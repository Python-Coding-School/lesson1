def fib(n):
    # if n == 0 or n == 1:
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib_pro(n):
    if n in cache:
        return cache[n]
    cache[n] = fib_pro(n-1) + fib_pro(n-2)
    return cache[n]

if __name__ == '__main__':
    n = int(input("Please give a number:"))
    
    cache = {0: 0, 1: 1}
    for i in range(1, n + 1):
        # print(i, '\t--->\t', fib(i))
        print(i, '\t--->\t', fib_pro(i))
