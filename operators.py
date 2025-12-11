#operators in python
#arithematic operations +,-,*,/,//,%
print("+,-,*,/,//,%")
a = 2
b = 3
print("using + :  ",a+b)
print("using - :  ",a-b)
print("using * :  ",a*b)
print("using / :  ",a/b)
print("using // :  ",a//b)
print("using % :  ",a%b)

#Relational operator <=,<,>=,>,==,!=
print("<=,<,>=,>,==,!=")
print(a<=b)
print(a<b)
print(a>=b)
print(a>b)
print(a==b)
print(a!=b)

#logical and, or, not
x = True
y = False
print(x and y)
print(x or y)
print(not a)

#bitwise operator
print("bitwise operator")
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

#assignment operator
print("assignment operator")
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

#identity operator
print("identity operator -is not, is")
p = 10
q = 20
r = p

print(p is not q)
print(r is p)

print("ternary operator")
m,n = 10,20
min = m if m>n else n
print(min)