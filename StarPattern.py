n = int(input("Enter a number: "))

print("Pattern -1")
for i in range(n,0,-1):
    print((n-i)*" "+i*"@")

print("Pattern-2")
i=0
for i in range(0,n+1):
    print((n-i)*" "+i*"@")

print("Pattern-3")
i=0
for i in range(n,0,-1):
    print((n-i)*" "+i*"@",end = "")
    print(i*"@")

print(n*" "+"@")
