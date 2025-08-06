danhsachcongviec=[]
while True:
    print("1.Thêm việc mới vào danh sách","2.Hien thi cong viec","3. Xoa viec","4.Thoat chuong trinh",sep="\n")
    hoi=int(input("Ban muon dung tinh nang so may?"))
    if hoi==1:
        themviec=input("ban co muon them viec moi khong? ")
        if themviec == "co":
            viec=input("them viec gi?")
            danhsachcongviec.append(viec)
            print(f"danh sach cong viec da them {danhsachcongviec}")
    elif hoi==2:
        print(danhsachcongviec)
    elif hoi==3:
        xoaviec=int(input("Ban muon xoa cong viec o so may?"))
        danhsachcongviec.pop(xoaviec-1)
        for i in danhsachcongviec:
            danhsachcongviec.pop(xoaviec-1)
            print(f"da xoa cong viec{danhsachcongviec}")
    elif hoi==4:
        break