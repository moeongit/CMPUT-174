average = float(input("Type the class average: "))
snacks = ""
if average <= 40:
    snacks = "Lollipops"
elif average <= 90:
    snacks = "Cookies"
else:
    snacks = "Ice Cream"

print(f"Bring {snacks}.")