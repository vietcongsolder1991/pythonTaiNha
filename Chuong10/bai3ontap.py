def timSoNguyenTo(so):
    check=0
    for i in range(2,so):
        if so%i ==0:
            check=1
    if check ==1:
        print("không phải là số nguyên tố")
    else:
        print("số nguyên tố")
timSoNguyenTo(5)