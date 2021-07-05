numbers = []
final = []
final_final = []
num = int(input('what is the number? '))
for i in range(1, num + 1):
    numbers.append(i)

max = sorted(numbers, reverse=True)
min = sorted(numbers)

max = int("".join(map(str, max)))
min = int("".join(map(str, min)))

for i in range(min, max + 1):
    i = str(i)
    check = False
    for j in i:
        if int(j) in numbers:
            check = True
        else:
            check = False
            break
    if check == True:
        final.append(i)

for number in final:
    check = set()
    for j in number:
        check.add(j)
    if len(check) > num - 1:
        final_final.append(number)

print(len(final_final))
for i in final_final:
    temp = []
    for j in i:
        temp.append(j)
    print(' '.join(temp))
