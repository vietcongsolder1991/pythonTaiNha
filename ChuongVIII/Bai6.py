tong = 0
a = 0 
# for i in scores:
#     tong = tong + i
#     print(i)
# print(f"{tong/len(scores)}")
while True:
    SoTrungBinh = input("Nhập các số để tính trung bình: ")
    if SoTrungBinh == "e":
        break
    else:
        Somoi= SoTrungBinh.split(" ")
        for i in Somoi:
            tong = tong+int(i)
        a = a+len(Somoi)
        print(f"{tong/a}")