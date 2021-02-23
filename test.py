rax, pox, six, sox = 0, 0, 0, 0
b = 573201

a=100000
while b > a:
    b -= a
    rax += 1
print(rax, b)

a=10000
while b > a:
    b -= a
    pox += 1
print(pox, b)

a=1000
while b > a:
    b -= a
    six += 1
print(six, b)

a=100
while b > a:
    b -= a
    sox += 1
print(sox, b)

print(rax*1000+pox*100+six*10+sox)