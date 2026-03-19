import math

# --- LỚP 1: ĐỊNH NGHĨA ĐỐI TƯỢNG SINH VIÊN ---
class SinhVien:
    def __init__(self, id, name, sex, age, diemToan, diemLy, diemHoa):
        self._id = id
        self._name = name
        self._sex = sex
        self._age = age
        self._diemToan = diemToan
        self._diemLy = diemLy
        self._diemHoa = diemHoa
        self._diemTB = 0
        self._hocLuc = ""

# --- LỚP 2: CÁC HÀM QUẢN LÝ ---
class QuanLySinhVien:
    def __init__(self):
        # Danh sách để lưu trữ các đối tượng SinhVien
        self.listSinhVien = []

    # Hàm tự động tạo ID tăng dần
    def generateID(self):
        maxId = 1
        if (len(self.listSinhVien) > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    # Hàm nhập sinh viên mới
    def nhapSinhVien(self):
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

    # Hàm cập nhật thông tin theo ID
    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if (sv != None):
            print(f"\n--- Cap nhat thong tin cho SV ID: {ID} ---")
            sv._name = input("Nhap ten moi: ")
            sv._sex = input("Nhap gioi tinh moi: ")
            sv._age = int(input("Nhap tuoi moi: "))
            sv._diemToan = float(input("Nhap diem toan moi: "))
            sv._diemLy = float(input("Nhap diem ly moi: "))
            sv._diemHoa = float(input("Nhap diem hoa moi: "))
            self.tinhDTB(sv)
            self.xepLoaiHocLuc(sv)
            print("Cap nhat thanh cong!")
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.")

    # Các hàm sắp xếp
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=True) # Sắp xếp giảm dần

    # Tìm kiếm theo ID
    def findByID(self, ID):
        for sv in self.listSinhVien:
            if (sv._id == ID):
                return sv
        return None

    # Tìm kiếm theo tên (gần đúng)
    def findByName(self, keyword):
        listResult = []
        for sv in self.listSinhVien:
            if (keyword.upper() in sv._name.upper()):
                listResult.append(sv)
        return listResult

    # Xóa sinh viên
    def deleteById(self, ID):
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            return True
        return False

    # Tính điểm trung bình
    def tinhDTB(self, sv):
        diemTB = (sv._diemToan + sv._diemLy + sv._diemHoa) / 3
        sv._diemTB = round(diemTB, 2)

    # Xếp loại học lực
    def xepLoaiHocLuc(self, sv):
        if (sv._diemTB >= 8): sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5): sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5): sv._hocLuc = "Trung Binh"
        else: sv._hocLuc = "Yeu"

    # Hiển thị danh sách
    def showSinhVien(self, listSV):
        print("\n{:<5} {:<20} {:<8} {:<5} {:<5} {:<5} {:<5} {:<8} {:<10}"
              .format("ID", "Ten", "G.Tinh", "Tuoi", "Toan", "Ly", "Hoa", "GPA", "Hoc Luc"))
        print("-" * 80)
        if (len(listSV) > 0):
            for sv in listSV:
                print("{:<5} {:<20} {:<8} {:<5} {:<5} {:<5} {:<5} {:<8} {:<10}"
                      .format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, 
                              sv._diemLy, sv._diemHoa, sv._diemTB, sv._hocLuc))
        else:
            print("Danh sach trong!")
        print("\n")

# --- CHƯƠNG TRÌNH CHÍNH (MAIN) ---
qlsv = QuanLySinhVien()

while True:
    print("\n========= CHUONG TRINH QUAN LY SINH VIEN =========")
    print("1. Them sinh vien")
    print("2. Cap nhat thong tin sinh vien theo ID")
    print("3. Xoa sinh vien theo ID")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem trung binh (GPA)")
    print("6. Sap xep sinh vien theo ten")
    print("7. Sap xep sinh vien theo ID")
    print("8. Hien thi danh sach sinh vien")
    print("0. Thoat chương trình")
    print("==================================================")
    
    try:
        choice = int(input("Chon chuc nang (0-8): "))
    except ValueError:
        print("Loi: Vui long nhap mot so tu 0 den 8!")
        continue

    if choice == 1:
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    
    elif choice == 2:
        if qlsv.soLuongSinhVien() > 0:
            id_input = int(input("Nhap ID can sua: "))
            qlsv.updateSinhVien(id_input)
        else:
            print("Danh sach dang trong!")
            
    elif choice == 3:
        if qlsv.soLuongSinhVien() > 0:
            id_del = int(input("Nhap ID can xoa: "))
            if qlsv.deleteById(id_del):
                print(f"Da xoa sinh vien ID {id_del}")
            else:
                print("Khong tim thay ID nay.")
        else:
            print("Danh sach dang trong!")
            
    elif choice == 4:
        name_search = input("Nhap ten can tim: ")
        result = qlsv.findByName(name_search)
        qlsv.showSinhVien(result)
        
    elif choice == 5:
        qlsv.sortByDiemTB()
        print("\nDanh sach sau khi sap xep theo GPA giam dan:")
        qlsv.showSinhVien(qlsv.listSinhVien)
        
    elif choice == 6:
        qlsv.sortByName()
        print("\nDanh sach sau khi sap xep theo ten (A-Z):")
        qlsv.showSinhVien(qlsv.listSinhVien)
        
    elif choice == 7:
        qlsv.sortByID()
        print("\nDanh sach sau khi sap xep theo ID tang dan:")
        qlsv.showSinhVien(qlsv.listSinhVien)
        
    elif choice == 8:
        print("\nDANH SACH SINH VIEN HIEN TAI:")
        qlsv.showSinhVien(qlsv.listSinhVien)
        
    elif choice == 0:
        print("Tam biet!")
        break
    else:
        print("Chuc nang khong hop le, vui long chon lai!")