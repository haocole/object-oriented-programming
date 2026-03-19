# class Student:
#     # Hàm khởi tạo thuộc tính
#     def __init__(self):
#         self.id = ""
#         self.name = ""

#     # Phương thức thêm sinh viên
#     def add(self):
#         self.id = input("Nhập mã sinh viên: ")
#         self.name = input("Nhập tên sinh viên: ")
#         print("=> Đã thêm thành công!")

#     # Phương thức hiển thị thông tin
#     def show(self):
#         if self.id == "":
#             print("=> Dữ liệu trống!")
#         else:
#             print(f"--- Thông tin: [ID: {self.id}] - [Tên: {self.name}] ---")

#     # Phương thức sửa sinh viên
#     def edit(self):
#         if self.id == "":
#             print("=> Không có gì để sửa!")
#         else:
#             self.name = input("Nhập tên mới: ")
#             print("=> Đã cập nhật thông tin!")

#     # Phương thức xóa sinh viên
#     def remove(self):
#         self.id = ""
#         self.name = ""
#         print("=> Đã xóa dữ liệu sinh viên!")

# # --- CHƯƠNG TRÌNH CHÍNH ---
# sv = Student() # Tạo đối tượng

# while True:
#     print("\n------ MENU QUẢN LÝ ------")
#     print("1. Thêm sinh viên")
#     print("2. Xem thông tin")
#     print("3. Sửa thông tin")
#     print("4. Xóa sinh viên")
#     print("0. Thoát")
    
#     chon = input("Mời bạn chọn số: ")

#     if chon == "1": sv.add()
#     elif chon == "2": sv.show()
#     elif chon == "3": sv.edit()
#     elif chon == "4": sv.remove()
#     elif chon == "0": break
#     else: print("Chọn sai, vui lòng chọn lại!")

class Student:
    # Hàm khởi tạo thuộc tính
    def __init__(self):
        self.id = ""
        self.name = ""

    # Phương thức thêm sinh viên
    def add(self):
        self.id = input("Nhập mã sinh viên: ")
        self.name = input("Nhập tên sinh viên: ")
        print("=> Đã thêm thành công!")

    # Phương thức hiển thị thông tin
    def show(self):
        if self.id == "":
            print("=> Dữ liệu trống!")
        else:
            print(f"--- Thông tin: [ID: {self.id}] - [Tên: {self.name}] ---")

    # Phương thức sửa sinh viên
    def edit(self):
        if self.id == "":
            print("=> Không có gì để sửa!")
        else:
            self.name = input("Nhập tên mới: ")
            print("=> Đã cập nhật thông tin!")

    # Phương thức xóa sinh viên
    def remove(self):
        self.id = ""
        self.name = ""
        print("=> Đã xóa dữ liệu sinh viên!")

# --- CHƯƠNG TRÌNH CHÍNH ---
sv = Student() # Tạo đối tượng

while True:
    print("\n------ MENU QUẢN LÝ ------")
    print("1. Thêm sinh viên")
    print("2. Xem thông tin")
    print("3. Sửa thông tin")
    print("4. Xóa sinh viên")
    print("0. Thoát")
    
    chon = input("Mời bạn chọn số: ")

    if chon == "1": sv.add()
    elif chon == "2": sv.show()
    elif chon == "3": sv.edit()
    elif chon == "4": sv.remove()
    elif chon == "0": break
    else: print("Chọn sai, vui lòng chọn lại!")