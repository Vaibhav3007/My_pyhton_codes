enter = input("Enter a number - ")
num = []
summation = 0

for i in range(len(enter)):
    num.append(int(enter[i]))

for j in range(len(num)):
    summation = summation+num[j]
        
print("Sum of digits of",enter,"is",summation)
