num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

nums = [num1,num2,num3]
#print(nums)


for i in range(3):
    for j in range(3):
        for k in range(3):
            if (i != j & j!= k & k!=i):
                #print((nums[i],i),(nums[j],j),(nums[k],k),end=" , ")
                """Uncomment above to understand in detail"""
                print(nums[i],nums[j],nums[k])

"""This code prints result when values of i,j,k are not equal and it takes there respective values
as the index for list and prints corresponding value"""
            
"""Further we can expand this code for non-repetetive numbers only in final output"""
