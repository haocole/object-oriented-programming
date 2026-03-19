class Dog:
    # Thuộc tính (Property)
    def __init__(self, color):
        self.color = color  # Gán màu sắc khi tạo con chó

    # Hành động (Method)
    def run(self):
        print("Con chó đang chạy")

# --- Cách chạy ---
my_dog = Dog("Vàng") # Tạo một đối tượng chó màu vàng
print(f"Màu của chó: {my_dog.color}")
my_dog.run() # Gọi hành động chạy