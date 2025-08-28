tong=1
while  True:
        try:
            x=int(input("nhập một số nguyên dương"))
        except:
            print("nhập lại")
            continue
        if x>0:
            for i in range(1,x+1):
                tong=i*tong
            print(tong)
            break
        else:
            print("nhập lại")