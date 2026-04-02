def updateSinhVien(self, ID):
    # Tìm kiếm sinh viên trong danh sách listSinhVien
    sv:SinhVien = self.findByID(ID)
    # Nếu sinh viên tồn tại thì cập nhập thông tin sinh viên
    if (sv != None):
        # nhập thông tin sinh viên
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        age = int(input("Nhap tuoi sinh vien: "))
        diemToan = float(input("Nhap diem toan: "))
        diemLy = float(input("Nhap diem Ly: "))
        diemHoa = float(input("Nhap diem Hoa: "))
        # cập nhật thông tin sinh viên
        sv._name = name
        sv._sex = sex
        sv._age = age
        sv._diemToan = diemToan
        sv._diemLy = diemLy
        sv._diemHoa = diemHoa
        self.tinhDTB(sv)
        self.xepLoaiHocLuc(sv)
    else:
        print("Sinh vien co ID = {} khong ton tai.".format(ID))
