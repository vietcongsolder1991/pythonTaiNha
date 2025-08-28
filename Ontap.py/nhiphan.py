x=int(input("nhập một số: "))
sonhiphan=[]
while x !=0:
    c= x%2
    sonhiphan.append(c)
    x=x//2
for i in range(len(sonhiphan)):
    sonhiphan[i]=str(sonhiphan[i])
somoi=sonhiphan[len(sonhiphan)-1::-1]
result="".join(somoi)
print(result)