even = []
for number in range (1, 101):
    if number % 5 == 0 or number % 7 == 0:
        if number % 2 == 0:
            even.append(number)
        else:
            print(number)
print(even)
average = sum(even)/len(even)
print(f"The average of all even numbers between 1 and 100 that are divisible by 5 is: {average}")