def factorial(n: int) -> int:
    if (n==1):
        return 1
    return n*factorial(n-1)

n = int(input())
print(factorial(n))

