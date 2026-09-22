so_dien = int(input())
tien = 0
if so_dien <= 50:
    tien = so_dien * 1800
elif so_dien <=100:
    tien = 50 * 1800 + (so_dien - 50) * 2000
else:
    tien = 50 * 1800 + 50 * 2000 + (so_dien - 100) * 2500
print(tien)
