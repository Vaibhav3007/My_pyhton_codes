num = int(input("Enter a number: "))
temp = num

summation = 0

while num > 0:
    i = num%10
    summation = 10*summation+i
    num = num//10

if summation == temp:
    print("Inputed number",temp,"is palindrome")
else:
    print("Inputed number",temp,"is not palindrome")


