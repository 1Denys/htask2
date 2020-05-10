a = '123'
print(a)
print(a[::-1])
print(type(a))

b = 5831
print(b)
c = 0
while b > 0:
    c = c*10 + b%10
    b//=10
print(c)
