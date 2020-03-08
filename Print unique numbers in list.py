numbers = [12, 3, 14, 15, 22, 45, 62, 88, 39, 17, 22, 12, 14, 12, 3, 22, ]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


