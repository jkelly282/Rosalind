dominant = 15
hetero = 21
recessive = 25

total = dominant + hetero + recessive

r_r = (recessive / total) * ((recessive - 1) / (total - 1))
h_h = (hetero / total) * ((hetero - 1) / (total - 1))
h_r = (hetero / total) * (recessive / (total - 1)) + (recessive / total) * (
        hetero / (total - 1)
)

recessive_total = r_r + h_h * 1 / 4 + h_r * 1 / 2
total = 1 - recessive_total
print(total)
print(recessive_total)
