num = int(input("Enter a number: "))
temp = num

summation = 0

while num > 0:
    i = num%10
    summation = summation+1
    num = num//10

print("No of digits in",temp,"are",summation)
