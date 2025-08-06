number = int(input("Nhập một số: "))
tong = 0
for i in range(1,number):
    if number %i==0:
        tong = tong + i
if tong == number:
    print("đây là số hoàn hảo")
else:
    print("đây kphai số hoàn hảo")