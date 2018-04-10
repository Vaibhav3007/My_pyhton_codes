check = [y for y in range(1,51) if (y%2 == 0 or y%3 == 0)]
check2 = [y for y in range(1,51) if (y%2 != 0 and y%3 != 0)]
print("Numbers divisible by 2 or 3 -\n",check)
print("Numbers not divisible by 2 or 3 -\n",check2)

