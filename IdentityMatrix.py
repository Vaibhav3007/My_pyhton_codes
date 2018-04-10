n = int(input("Enter a number: "))
i=0
j=0

I = []



for i in range(n):
    for j in range(n):
        if (i == j):
            I.append(1)
        else:
            I.append(0)
print(I)
"""for x in range(0,n):
    print(I[x],end = " ")"""
