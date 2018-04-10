num = int(input("Enter a number: "))
summation = 0
temp = 1

while(temp<=num):
    nums = []

    for count in range(1,temp+1):
        print(count,sep = " ",end = " ")
        if (count < temp):
            print("+",sep = " ",end = " ")
        nums.append(count)
    print("=",sum(nums))
    temp += 1

"""for j in range(1,num+1):
    a=[]
    for i in range(1,j+1):
        print(i,sep=" ",end=" ")
        if (i<j):
            print("+",sep=" ",end=" ")
        a.append(i)
    print("=",sum(a))"""
        



    
