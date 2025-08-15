while True:
    x=input("nhập mật khẩu")
    if len(x)>8:
        for i in x:
            a= i in "}!@#$%^&*()~_{:?>"
        for so in x:
            b= so in "1234567890"
        for chu in x:
            c= chu in "ABCDEFGHKJDHQPOIPLKZXCVBNMNLKJHGFDSAQWERTYUIOP"
        if c==True and a == True and b==True:
            print("đã tạo mk")
            break