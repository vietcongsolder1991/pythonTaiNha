def dangnhap(user,password):
    while True:
        TenTaiKhoan=input("nhập tên:")
        MatKhau=input("nhap mk: ")
        if TenTaiKhoan==user and MatKhau == password:
            print("dang nhap thanh cong")
            break
        else:
            print("nhap lai")
dangnhap("admin","123456")