x=int(input("nhập một số: "))
while x%2!=0:
    try:
        x=int(input("nhập lại"))
    except ValueError:
        print("đó không phải là một số nhập lại")
print(f"bạn đã nhập số {x}")