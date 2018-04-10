num = int(input("Enter a number: "))
temp = num

summation = 0

while num > 0:
    i = num%10
    summation = summation+i
    num = num//10

print("Sum of digits in",temp,"is",summation)
