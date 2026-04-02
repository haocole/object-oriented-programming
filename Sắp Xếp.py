#Hàm sắp xếp danh sach sinh vien theo tên tăng dần
def sortByName(self):
    self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
