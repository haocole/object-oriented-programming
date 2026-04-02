# Hàm hiển thị danh sách sinh viên ra màn hình console
def showSinhVien(self, listSV):
    # hien thi tieu de cot
    print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
          .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
    # hien thi danh sach sinh vien
    if (listSV.__len__() > 0):
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                  .format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, 
                          sv._diemHoa,sv._diemTB, sv._hocLuc))
    print("\n")