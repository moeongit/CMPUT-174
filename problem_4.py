mark = float(input("Enter Mark: "))
grade = ""

if mark <= 50:
    grade = "F".upper()
elif mark <= 60:
    grade = "D".upper()
elif mark <= 70:
    grade = "C".upper()
elif mark <= 80:
    grade = "B".upper()
else:
    grade = "A".upper()

if mark < 0 or mark > 100:
    print("Mark is invalid.")

print("The grade for the mark " + str(mark) + " is " + grade + ".")