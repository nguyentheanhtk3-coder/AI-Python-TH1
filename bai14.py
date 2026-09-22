import random
n = random.randint(1, 10)
print("Đoán số ngẫu nhiên từ 1 đến 10")
while True:
    i = int(input())
    if i > n:
        print("Số bạn nhập lớn hơn số ngẫu nhiên")
    elif i < n:
        print("Số bạn nhập nhỏ hơn số ngẫu nhiên")
    else:
        print("Chúc mừng! Bạn đã đoán đúng.")
        break