m = input("Enter marks of subjetcs out of 100: ")
marks = [int(x) for x in m.split(" ")]
total = 0

for i in range(len(marks)):
    total = total + marks[i]
    

percent = total/len(marks)

print("Marks = ", marks)
print("Percentage = ",percent)

if percent >= 90:
    print("Grade obtained - A+")
elif percent >=80 and percent <90:
    print("Grade obtained - A")
elif percent >= 70 and percent <80:
    print("Grade obtained - B+")
elif percent >= 60 and percent <70:
    print("Grade obtained - B")
elif percent >=50 and percent < 60:
    print("Grade obtained - C")
else:
    print("Grade obtained - F")
