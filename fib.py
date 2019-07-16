num = int(input("Enter a number: "))

def fibonacci(n):
    if n < 2:               
        return n
    return fibonacci(n-2) + fibonacci(n-1)
print(list(map(fibonacci, range(1, num+1))))