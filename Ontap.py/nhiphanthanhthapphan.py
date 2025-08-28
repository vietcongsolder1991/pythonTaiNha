x=str(input("nhập số nhị phân"))
so=[]
somoi=0
for i in range(len(x)):
    y=int(x[i])
    so.append(y)
for a in range(len(so)):
    somoi=somoi*2+so[a]
print(somoi)