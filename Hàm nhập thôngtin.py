def nhapSinhVien(self):
    # Khởi tạo một sinh viên mới
    svId = self.generateID()
    name = input("Nhap ten sinh vien: ")
    sex = input("Nhap gioi tinh sinh vien: ")
    age = int(input("Nhap tuoi sinh vien: "))
    diemToan = float(input("Nhap diem toan: "))
    diemLy = float(input("Nhap diem Ly: "))
    diemHoa = float(input("Nhap diem Hoa: "))
    sv = SinhVien(svId, name, sex, age, diemToan, diemLy, diemHoa)
    self.tinhDTB(sv)
    self.xepLoaiHocLuc(sv)
    self.listSinhVien.append(sv)