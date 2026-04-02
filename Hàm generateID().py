# Hàm tạo ID tăng dần cho nhân viên
def generateID(self):
    maxId = 1
    if (self.soLuongSinhVien() > 0):
        maxId = self.listSinhVien[0]._id
        for sv in self.listSinhVien:
            if (maxId < sv._id):
                maxId = sv._id
        maxId = maxId + 1
    return maxId