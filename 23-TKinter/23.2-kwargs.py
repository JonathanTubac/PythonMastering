def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,5,6,7,8,9,4,5,6))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["mult"]
    print(n)

calculate(2, add=3, mult=5)