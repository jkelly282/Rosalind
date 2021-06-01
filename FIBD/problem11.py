import argparse
from collections import defaultdict


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', dest="generations", default=83, help="Number of generations")
    parser.add_argument('-d', dest="mortality_rate", default=20, help="Number of months Rabbits alive")
    args = parser.parse_args()
    return args


def calculate_number_rabbits(generations, mortality_rate):
    current_gen = defaultdict(int)
    for i in range(1, mortality_rate + 1):
        current_gen[i] = 0
    new_rabbits = 0
    for i in range(generations):
        print(i)
        if i == 0:
            current_gen[1] = 1
        elif i == 1:
            current_gen[1] = 0
            current_gen[2] = 1
        else:
            for k, v in list(current_gen.items()):
                if k == 1:
                    if v:
                        current_gen[k] -= v
                        current_gen[k + 1] += v

                elif k < mortality_rate and k > 1:
                    current_gen[k] -= v
                    current_gen[k + 1] += v
                    current_gen[1] += v

                elif k == mortality_rate:
                    current_gen[1] += v
                    current_gen[k] -= v
    return current_gen


if __name__ == '__main__':
    args = parse_args()
    current_gen = calculate_number_rabbits(args.generations, args.mortality_rate)
    total = 0
    for k, v in current_gen.items():
        total += v
    print(total)

"""
    for i in range(generations):
        if i <= 3:
            n1 = 2
            n2= 2
            n3 =1
            rabbits =2
        else:

            n1 = rabbits
            rabbits = n2 + n3
            n3 = n2
            n2 = n1


    return rabbits
"""

"""
def calculate_number_rabbits(generations, mortality_rate):
    rabbits_alive = []
    rabbits_died_this_gen = 0
    for i in range(generations):
        if i == 0 or i ==1:
            n1 = 1
            n2 =1
            if i ==0:
              rabbits_alive.append(([1]))
            else:
                rabbits_alive[0][0]+=1
        else:
            rabbits_died_last_gen = rabbits_died_this_gen
            rabbits_died_this_gen = 0
            for j,l in enumerate(rabbits_alive[:]):
                l[0] +=1
                if l[0] == mortality_rate+1:
                    rabbits_alive.remove(rabbits_alive[j])
                    rabbits_died_this_gen +=1
            if i < 3:
                rabbits = (n1+n2)
            else:
                rabbits = (n1 + n2) - (rabbits_died_this_gen+rabbits_died_last_gen)
            rabbits_born = n2
            for k in range(rabbits_born):
                rabbits_alive.append([1])
            n2 =n1
            n1 = rabbits
    return rabbits
"""

"""
        if i == 0 or i ==1:
            n1 = 1
            n2 =1
            if i ==0:
              rabbits_alive.append(1)
            else:
                rabbits_alive[0]+=1
        else:
            for j,l in enumerate(rabbits_alive[:]):
              rabbits_alive[j] +=1

            rabbits_alive = [rabbit for rabbit in rabbits_alive if rabbit <= mortality_rate+1]

            if i < 3:
                rabbits = n1+n2
                rabbits_born = n2
            else:
                rabbits = len(rabbits_alive)
                rabbits_born = n2

            for k in range(rabbits_born):
                rabbits_alive.append(1)
            n2 =n1
            n1 = rabbits
"""

"""
    for i in range(generations):
            baby_rabbits = 0
            mature_rabbits = 0
            dead_rabbits = 0
            if i >= 1:
              current_gen = next_gen
              next_gen = []
            for check in current_gen:
                if check ==1:
                    next_gen.append(2)
                    mature_rabbits +=1
                elif check < mortality_rate and check > 1:
                    next_gen.append(check+1)
                    next_gen.append(1)
                    baby_rabbits +=1
                    mature_rabbits +=1
                elif check == mortality_rate:
                    next_gen.append(1)
                    dead_rabbits +=1

            total_rabbits = (baby_rabbits+mature_rabbits+dead_rabbits)
            print(f'total_rabbits = {total_rabbits}')
"""

"""
def calculate_number_rabbits(generations, mortality_rate):
    next_gen = []
    current_gen = [1]

    for i in range(generations):
            baby_rabbits = 0
            mature_rabbits = 0
            dead_rabbits = 0
            if i >= 1:
              current_gen = next_gen
              next_gen = []
            for check in current_gen:
                if check < mortality_rate and check > 1:
                    next_gen.append(check+1)
                    next_gen.append(1)
                elif check ==1:
                    next_gen.append(2)
                elif check == mortality_rate:
                    next_gen.append(1)
            print(i)
    return current_gen
"""

"""
    next_gen = []
    current_gen = [1]

    for i in range(generations):

            if i >= 1:
                current_gen = next_gen
                next_gen = []

            baby = sum(map(lambda x : x == 1, current_gen))
            mature_rabbits = [ x+1 for x in current_gen if x <mortality_rate and x >1 ]
            elder = len(current_gen) - (baby+len(mature_rabbits))


            next_gen += baby * [2]
            next_gen += len(mature_rabbits) *[1]
            next_gen.extend(mature_rabbits)
            next_gen += elder * [1]
            print(i)

    return current_gen
"""

"""
    for i in range(generations):
        if i == 0 or i == 1:
            n_one = 1
            n_two = 1
        else:
            a = n_one + n_two
            n_two = n_one
            n_one = a
            print(a)
            """
