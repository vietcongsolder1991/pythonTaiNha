a=int(input("Nhập một số a: "))
b = int(input("nhập một số b: "))
c=int(input("Nhập một số c: "))
def UCLN(a,b):
    if a<b:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                return(i)
    else:
        for e in range(b,0,-1):
            if b%e==0 and a%e==0:
                return(e)
print(UCLN(UCLN(a,b),c))