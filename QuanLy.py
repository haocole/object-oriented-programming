class SinhVien:
    def __init__(self, ms, hoten, dlt, dth):
        self.ms = ms
        self.hoten = hoten
        self.dlt = dlt
        self.dth = dth

    # Hàm tính điểm trung bình
    def diem_tb(self):
        return (self.dlt + self.dth) / 2

    # Hàm hiển thị thông tin
    def hien_thi(self):
        dtb = self.diem_tb()
        print(f"{self.ms:<10} | {self.hoten:<20} | LÝ THUYẾT: {self.dlt:<5} | THỰC HÀNH: {self.dth:<5} | ĐTB: {dtb:.2f}")

dssv = []
n = int(input("Nhập số lượng sinh viên muốn thêm: "))

for i in range(n):
    print(f"\n--- Nhập sinh viên thứ {i+1} ---")
    ms = input("Mã số sinh viên: ")
    hoten = input("Họ và tên: ")
    dlt = float(input("Điểm lý thuyết: "))
    dth = float(input("Điểm thực hành: "))
    
    sv = SinhVien(ms, hoten, dlt, dth)
    dssv.append(sv)

print("\n" + "="*85)
print(f"{'MS':<10} | {'HỌ TÊN':<20} | {'LÝ THUYẾT':<16} | {'THỰC HÀNH':<16} | {'ĐTB'}")
print("-" * 85)
for sv in dssv:
    sv.hien_thi()
 
# Tìm sinh viên điểm cao nhất
if dssv:
    sv_max = max(dssv, key=lambda sv: sv.diem_tb())
    print("\n" + "*"*30)
    print("SINH VIÊN CÓ ĐIỂM CAO NHẤT:")
    sv_max.hien_thi()
    print("*"*30)

# Sắp xếp theo tên
dssv.sort(key=lambda sv: sv.hoten)

print("\n--- DANH SÁCH SAU KHI SẮP XẾP THEO TÊN (A-Z) ---")
for sv in dssv:
    sv.hien_thi()

# Tính trung bình cả lớp
if dssv:
    tong_diem_lop = sum(sv.diem_tb() for sv in dssv)
    print(f"\n==> ĐIỂM TRUNG BÌNH CỦA CẢ LỚP: {tong_diem_lop / len(dssv):.2f}")






    