while True:
    a=0
    b=0
    c=0
    d=0
    mk=input("nhập mk đủ mạnh: ")
    for i in mk:
        if i in "1234567890":
            a=1
        elif i in "QWERTYUIOPASDFGHJKLZXCVBNM":
            b=1
        elif i in "~!@#$%^&*(())_+\{\}:?>}|":
            c=1
        elif len(mk)>=8:
            d=1
    if a==1 and b==1 and c==1 and d==1:
        print("đã tạo")
        break
    else:
        print("chưa đủ mạnh")