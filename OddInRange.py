start = int(input("Enter starting range - "))
end = int(input("Enter ending range - "))


nums = [x for x in range(start,end+1)]
new = []
j = 0
for i in range(len(nums)):
    remainder = nums[i]%2
    if remainder == 1:
        #create a new list and store
        new.append(nums[i])
    
print("Odd Numbers between",start,"&",end,"are")
print(new)
