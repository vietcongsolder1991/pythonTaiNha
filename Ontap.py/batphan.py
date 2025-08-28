x=int(input("nhập một số: "))
sonhiphan=[]
while x !=0:
    c= x%8
    sonhiphan.append(c)
    x=x//8
for i in range(len(sonhiphan)):
    sonhiphan[i]=str(sonhiphan[i])
somoi=sonhiphan[len(sonhiphan)-1::-1]
result="".join(somoi)
print(result)