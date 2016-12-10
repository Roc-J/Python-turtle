def square(x):
    y = x*x
    return y

def sum_of_square(x,y,z):
    a = square(x)
    b = square(y)
    c = square(z)

    return a+b+c

a = -5
b = 10
c = 2

result = sum_of_square(a,b,c)
print result