n = input('Please enter number of months: ')
k = input('Please enter the number of rabbit pairs produced each generation: ')
a = 0
n_one = 0
n_two = 0

for i in range(int(n)):
    if i == 0 or i == 1:
        n_one = 1
        n_two = 1
    else:
        a = n_one + (n_two * int(k))
        n_two = n_one
        n_one = a

print(a)
