start = int(input("Enter starting range - "))
end = int(input("Enter ending range - "))

odd = [x for x in range(start,end+1) if x%2==1]
print("Odd numbers between",start,"and",end,"are\n",odd)
