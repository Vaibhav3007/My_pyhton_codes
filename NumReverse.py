num = int(input("Input a number : "))
num1 = num
#num = 128
rev = 0

while (num > 0):
    i = num % 10
    rev = 10*rev + i
    num = num//10

print("Reverse of ",num1,"is ",rev)
if num1 == rev:
    print("And it is a palindrome")
