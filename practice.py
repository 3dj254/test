#arithemetic operators
x=5
y=2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y) #the floor division // rounds the result down to the nearest whole number

# ASsignment 0perators
x=5
print(x)

x=5
x+=3
print(x)

x=5
x-=3
print(x)

x=5
x*=3
print(x)

x=5
x/=3
print(x)

x=5
x%=3
print(x)

x=5
x//=3
print(x)

x=5
x**=3
print(x)

x=5
x&=3
print(x)

x=5
x&=3
print(x)

x=5
x|=3
print(x)

x=5
x^=3
print(x)

x=5
x<<=3
print(x)

x=5
x>>=3
print(x)

print(x:=3)

#comparison operators
x=2
y=3
print(x==y)

x=2
y=3
print(x!=y)

x=2
y=3
print(x>y)

x=2
y=3
print(x<y)

x=2
y=3
print(x<=y)

x=2
y=3
print(x<=y)

#logical operators used to combine conditional statements
x=3
print(x<5 and x<10)
 
x=3
print(x<5 or x<4)

x=3
print(not(x<5 and x<10))
#Identity operators
x=3
y=3.0
print(x is y)

x=3
y=3.0
print(x is not y)
#Membership operators
x=['ovacado','banana']
print('banana' in x)
#Bitwise operators
print(6 & 3)
print(6|3)
print(6^3)
print(~3)
print(3<<2)
print(8>>2)

#operator precedence
print((6+3)-(6+3))
print(100 + 5 * 3)