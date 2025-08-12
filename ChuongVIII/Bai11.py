Kytu="*"
def hinhvuong(a,b):
    for i in range(a):
        for j in range(b):
            print(f"{Kytu}",end=" ")
        print()
a = int(input("số hàng: "))
b = int(input("số cột: "))
hinhvuong(a,b)