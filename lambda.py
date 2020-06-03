"""def square(num):
	return num**2

print(square(numbers))"""
"""
numbers = [1,2,3,4,5,6,7,8,9,10]

def square(num):
	return num**2
result = list(map(square, numbers))
print(result[2])

for item in map(square, numbers):
	print(item)"""
"""
numbers = [1,2,3,4,5,6,7,8,9,10]

def square(num):
	return num**2
result = list(map(lambda num: num**2, numbers))
print(result[2])"""
numbers = [1,2,3,4,5,6,7,8,9,10]
def checkeven(num):	return num%2==0

check = lambda num: num%2==0

result = list(filter(check ,numbers))
print(result)

