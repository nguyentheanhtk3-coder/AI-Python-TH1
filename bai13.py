dem = 0
n = int(input("Nhập số n: "))
for i in range(1, n+1):
    a = int(input())
    if a % 2 == 0:
        dem += 1
print(dem)