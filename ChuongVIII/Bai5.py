# for i in range(100,0,-1):
#     print(i)
# # print("bat dau")
# for i in range(1,101):
#         for a in range(1,i):
#             if a*a ==i:
#                   print(i)
#             else:
#                   continue
# for i in range(1,101):
#     a= i*i
#     if a<=100:
#         print(a)
#     else:
#         continue
import math 
SoCP = int(input("Nhập một số: "))
Somoi=int(math.sqrt(SoCP))
if Somoi**2==SoCP:
    print(SoCP)
else:
    print("khong phai so chinh phuong")