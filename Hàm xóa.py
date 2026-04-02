# Hàm xóa sinh viên theo ID
def deleteById(self, ID):
    isDeleted = False
    # tìm kiếm sinh viên theo ID
    sv = self.findByID(ID)
    if (sv != None):
        self.listSinhVien.remove(sv)
        isDeleted = True
    return isDeleted