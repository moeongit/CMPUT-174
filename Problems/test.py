filename = 'employees_t.txt'
mode = 'r'
pay_rate = 20
weekly_hours = []
employees = []
above_average = []
with open (filename, mode) as file:
    list_of_lines = file.readlines()
for line in list_of_lines:
    line = line.strip()
    record = line.split()
    if record:
        name = record[0]
        hours = 0
        for index in range(1, len(record)):
            hours = hours + int(record[index])
    print(f"{name} {hours} ${hours} * {pay_rate}")
    weekly_hours.append(hours)
print(employees)
print(weekly_hours)
average = sum(weekly_hours)/len(weekly_hours)
print(average)
for index in range(len(weekly_hours)):
    if weekly_hours[index] > average:
        above_average.append(employees[index])
print(''.join(above_average))