tong = 0
# SoThuTu=input("Nhập các số từ bàn phím (cách nhau bằng dấu cách):")
# Somoi= SoThuTu.split(" ")
# for i in Somoi:
#     tong = int(i)+tong
# print(tong)
# while True:
#     SoThuTu = input("Nhập số từ bàn phím (Nhập e để kết thúc)")
#     if SoThuTu =="e":
#         break
#     else:
#         tong = tong+int(SoThuTu)
# print(tong)
while True:
    SoThuTu = input("Nhập các số từ bàn phím cách nhau bằng dấu cách (muốn kết thúc, hãy nhấn e): ")
    if SoThuTu == "e":
        break
    else:
        SoMoi=SoThuTu.split(" ")
        for i in SoMoi:
            tong = tong+ int(i)
print(tong)