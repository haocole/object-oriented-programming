# Hàm tìm kiếm sinh viên theo tên
# Trả về một danh sách sinh viên
def findByName(self, keyword):
    listSV = []
    if (self.soLuongSinhVien() > 0):
        for sv in self.listSinhVien:
            if (keyword.upper() in sv._name.upper()):
                listSV.append(sv)
    return listSV