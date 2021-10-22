def factorial(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
        yield f


n = int(input('Enter number: '))
for elem in (factorial(n)):
    print(elem)
