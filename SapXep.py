# Hàm sắp xếp danh sach sinh vien theo điểm TB tăng dần
def sortByDiemTB(self):
    self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
