class Student:
    # 1. Thuộc tính (Property): Dùng hàm __init__ để khởi tạo dữ liệu ban đầu
    def __init__(self):
        self.id = ""
        self.name = ""

    # 2. Hành động (Method): Phương thức thêm sinh viên
    def add(self, id, name):
        print("--- Đang thực hiện hàm add ---")
        self.id = id
        self.name = name

    # 3. Hành động: Phương thức hiển thị thông tin
    def show(self):
        print(f"Kết quả -> ID: {self.id}, NAME: {self.name}")

# --- PHẦN CHẠY CHƯƠNG TRÌNH ---
# Bước 1: Tạo đối tượng cụ thể từ Class Student
sv1 = Student()

# Bước 2: Gọi phương thức add để nhập dữ liệu
sv1.add("SV001", "Hào")

# Bước 3: Gọi phương thức show để xem kết quả
sv1.show()
