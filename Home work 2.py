#home work 1

print("Hello, this is my homework =)")
number = int(input("Enter a number: "))

n1 = number // 1000
n2 = number % 1000 // 100
n3 = number % 100 // 10
n4 = number % 10

print(n1)
print(n2)
print(n3)
print(n4)

#home work2


number = int(input("Enter a number: "))

n1 = number // 10000 % 10
n2 = number // 1000 % 10
n3 = number // 100 % 10
n4 = number // 10 % 10
n5 = number % 10

result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
print(result)