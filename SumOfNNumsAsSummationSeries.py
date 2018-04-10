num = int(input("Enter a number: "))
summation = 0
nums = []

for count in range(1,num+1):
    print(count,sep =" ",end=" ")#This prints 1 then goes to if which prints +
    if (count < num):
        print("+",sep = " ",end=" ")# this stops printing + when count reaches num
    nums.append(count)

print("=",sum(nums))
        
