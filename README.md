# 📘 Object-Oriented Programming (OOP)

<p align="center">
  🚀 Ghi chú và ví dụ về lập trình hướng đối tượng bằng Python
</p>

---

## 📌 Mục lục
- [Giới thiệu](#-giới-thiệu)
- [Khái niệm cơ bản](#-khái-niệm-cơ-bản)
- [Tính chất OOP](#-tính-chất-oop)
- [Ví dụ](#-ví-dụ)
- [Tổng kết](#-tổng-kết)

---

## 📖 Giới thiệu

Repository này dùng để:
- 📚 Lưu kiến thức học OOP
- 💻 Code ví dụ minh họa
- 🔁 Ôn tập dễ dàng

---

## 🧠 Khái niệm cơ bản

### 🔹 Object (Đối tượng)
- Có **thuộc tính** và **phương thức**

### 🔹 Attribute (Thuộc tính)
- Thông tin của đối tượng

### 🔹 Method (Phương thức)
- Hành động của đối tượng

### 🔹 Class (Lớp)
- Khuôn mẫu tạo đối tượng

---

## 🔥 Tính chất OOP

### 🔸 Abstraction
- Ẩn chi tiết, chỉ hiển thị phần cần thiết

### 🔸 Encapsulation
- Đóng gói dữ liệu

### 🔸 Inheritance
- Kế thừa từ lớp cha

### 🔸 Polymorphism
- Một hành động, nhiều cách thực hiện

---

## 💻 Ví dụ

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Gâu gâu")

dog = Dog()
dog.speak()

# 💻 Ví dụ Python

```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello", self.name)

p1 = Person("Hao")
p1.say_hello()
