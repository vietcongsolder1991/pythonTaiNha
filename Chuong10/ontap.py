danhsachcongviec=[]
def DanhSach():
    a = 0
    for i in danhsachcongviec:
        a=a+1
        print(f"{a}.{i}")
def ThemViec():
    DanhSach()
    themviec=input("ban co muon them viec moi khong?: ")
    if themviec == "co":
        viec=input("them viec gi?")
        danhsachcongviec.append(viec)
        print(f"danh sach cong viec da them {danhsachcongviec}")
def XoaViec():
    DanhSach()
    xoaviec=int(input("Ban muon xoa cong viec o so may?"))
    danhsachcongviec.pop(xoaviec-1)
    print(f"da xoa cong viec{danhsachcongviec}")
while True:
    print("1.Thêm việc mới vào danh sách","2.Hien thi cong viec","3. Xoa viec","4.Thoat chuong trinh",sep="\n")
    hoi=int(input("Ban muon dung tinh nang so may?"))
    if hoi==1:
        ThemViec()
    elif hoi==2:
        DanhSach()
    elif hoi==3:
        XoaViec()
    elif hoi==4:
        break