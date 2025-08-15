x = input("Nhập một câu: ")
y=[]
for i in x:
    if i in y:
        continue
    y.append(i)
    print(i,x.count(i))
print(y)