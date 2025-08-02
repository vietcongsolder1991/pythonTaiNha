n=0
while n<=0:
    try:
        n=int(input("Nhập một số dương: "))
    except ValueError:
        print("Nhập lại")
print(1+n)