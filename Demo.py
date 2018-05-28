# Python ML program

x = int(input("Input number 1 : "))
y = int(input("Input number 2 : "))

if x > y:
    print("Max number : ", x)
else:
    print("Max number : ", y)

print("Sum : ", x + y)
print("Sub : ", x - y)
print("Mul : ", x * y)
print("Div : ", x / y)
print("Mod : ", x % y)

for i in range(0, 10, 1):
    print("*"*i)
