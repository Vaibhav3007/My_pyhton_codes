num = int(input("enter a number greater than 1: "))
count = 2

while count <= num:
    if num%count == 0:
        print("Smallest divisor of",num,"is",count)
        break
    else:
        count += 1
