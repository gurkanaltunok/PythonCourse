# def square(num): return num ** 2
square = lambda num: num ** 2

numbers = [1,3,5,9,4,10]

# result = list(map(lambda num: num **2, numbers))
result = list(map(square, numbers))


# for number in map(square, numbers):
#     print(number)

# def check_even(num):
#     return num %2 == 0
check_even = lambda num: num%2 == 0

# result = list(filter(lambda num: num%2==0, numbers))

result = check_even(numbers[2])

print(result)
