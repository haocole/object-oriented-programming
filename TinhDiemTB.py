# Hàm tính điểm TB cho sinh viên
def tinhDTB(self, sv:SinhVien):
    diemTB = (sv._diemToan + sv._diemLy + sv._diemHoa) / 3
    # làm tròn điểm trung binh với 2 chữ số thập phân
    sv._diemTB = math.ceil(diemTB * 100) / 100
    #Hàm xếp loại học lực cho nhân viên
def xepLoaiHocLuc(self, sv:SinhVien):
    if (sv._diemTB >= 8):
        sv._hocLuc = "Gioi"
    elif (sv._diemTB >= 6.5):
        sv._hocLuc = "Kha"
    elif (sv._diemTB >= 5):
        sv._hocLuc = "Trung Binh"
    else:
        sv._hocLuc = "Yeu"