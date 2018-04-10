print("Enter numbers")
nums = [int(x) for x in input().split(" ")]
add = 0
n = len(nums)

for i in range(n):
    add = add + nums[i]

avg = add/n
print("Entered numbers are :", nums)
print("Average is :",avg)
