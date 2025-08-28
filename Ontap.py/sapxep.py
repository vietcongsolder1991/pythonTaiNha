so = [1,8,7,4,3,5,7,98,87,23,46,8,6,9,10,11,12,16]
def sap_xep():
    print(so)
    x=input("Sắp xếp tăng hay giảm(T/G)? ")
    for i in range(len(so)):
        for a in range(i+1,len(so)):
            if x=="T":
                if so[i] >so[a]:
                    c=so[i]
                    d=so[a]
                    so[i]=d
                    so[a]=c
            elif x=="G":
                if so[i] <so[a]:
                    c=so[i]
                    d=so[a]
                    so[i]=d
                    so[a]=c
    print(so)
sap_xep()
