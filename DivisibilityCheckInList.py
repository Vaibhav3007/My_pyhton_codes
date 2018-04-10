start = int(input("Enter starting range - "))
end = int(input("Enter ending range - "))
check = int(input("Check divisibility by - "))

nums = [x for x in range(start,end+1)]
new = []
j = 0
for i in range(len(nums)):
    div = nums[i]%check
    if div == 0:
        #print(nums[i],end=",")
        #create a new list and store
        new.append(nums[i])
        #print(new)
        #j = j+1
    else:
        continue
print("Numbers between",start,"&",end,"divisible by",check,"are")
print(new)
