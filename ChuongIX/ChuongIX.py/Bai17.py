def timso():
        a=input("Nhập số (cach nhau bang dau cach):")
        b=a.split(" ")
        return(b)
def cong():
    tong = 0
    b=timso()
    for i in b:
        tong = tong+int(i)
    print(tong)
def tru():
    b=timso()
    hieu= int(b[0])-int(b[1])
    print(hieu)
def nhan():
    b=timso()
    x = int(b[0])*int(b[1])
    print(x)
def chia():
    b= timso()
    chia=int(b[0])/int(b[1])
    print(chia)
while True:
    print(f"1.cong 2.Tru 3.Nhan 4.Chia 5.Thoat",sep="/n")
    hoi=int(input("ban chon chuc nang so may?: "))
    if hoi == 1:
        cong()
    elif hoi ==2:
        tru()
    elif hoi==3:
        nhan()
    elif hoi ==4:
        chia()
    else:
        break