DanhSachSinhVien=[]
Diem = []
DiemTrungBinh = []
def diem():
    themdiem = input("Nhập tất cả điểm cho sinh viên này( cách nhau bằng dấu cách): ")
    themdiemmoi = themdiem.split(" ")
    Diem.append(themdiemmoi)
def TrungBinh():
    a=0
    for DiemTungSinhVien in Diem:
        b = 0
        for TungDiem in DiemTungSinhVien:
            b=b+int(TungDiem)
        trungbinh = b/len(DiemTungSinhVien)
        print(f"{DanhSachSinhVien[a]} {trungbinh}")
        a +=1
def danhsach():
    a = 0
    for i in DanhSachSinhVien:
        a = a+1
        print(f"{a}.{i}", sep = "/n")
def ThemNguoi():
    them = input("Bạn có muốn thêm người không?: ")
    if them == "có":
        SinhVien= input("Tên của sinh viên?: ")
        DanhSachSinhVien.append(SinhVien)
        diem()
        danhsach()
        print(f"Đã thêm vào danh sách")
def XoaNguoi():
    xoa = input("Bạn có muốn xoá không?: ")
    if xoa == "có":
        danhsach()
        xoasinhvien = int(input("Bạn muốn xoá người ở thứ tự nào?: "))
        DanhSachSinhVien.pop(xoasinhvien-1)
        Diem.pop(xoasinhvien - 1)
        danhsach()
while True:
    print(f"1. Thêm người và điểm \n 2.Xoá người \n 3. danh sách sinh viên \n 4. Danh sách sinh viên gồm điểm trung bình")
    hoi = int(input("Bạn chọn tính năng mấy?: "))
    if hoi == 1:
        ThemNguoi()
    if hoi == 2:
        XoaNguoi()
    if hoi == 3:
        danhsach()
    if hoi ==4:
        TrungBinh()