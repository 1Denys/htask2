a = ('7887')
b = a[::-1]
if b ==a:
    print('Numbers are palinrome')
else:
    print('Numbers are not palinrome')

c = 7423
d = c + 0
print(c)
f = 0
while c > 0:
    f = f*10 + c%10
    c//=10
print(f)
if f == d:
    print('Numbers are palinrome')
else:
    print('Numbers are not palinrome')

