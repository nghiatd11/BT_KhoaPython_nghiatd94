# Bài 1: Tính Đóng gói (Encapsulation) - Chiếc Điện thoại
# Ý tưởng: Một chiếc điện thoại che giấu đi các chi tiết phức tạp bên trong (pin, chip xử lý).
# -- Bạn chỉ tương tác với nó qua các nút bấm hoặc màn hình. Bài tập này sẽ mô phỏng việc đó.
# Đề bài: Viết một class Phone để quản lý dung lượng pin.
# Trong hàm khởi tạo __init__, tạo một thuộc tính private tên là __battery_level và gán giá trị mặc định là 100.
# Viết một phương thức public tên là use_app(self, hours):
# Mỗi giờ sử dụng sẽ làm giảm __battery_level đi 10.
# Nếu pin xuống dưới 0, hãy gán nó bằng 0.
# Viết một phương thức public tên là charge_phone(self, hours):
# Mỗi giờ sạc sẽ làm tăng __battery_level lên 20.
# Nếu pin vượt quá 100, hãy gán nó bằng 100.
# Viết một phương thức public tên là display_battery(self) để in ra dung lượng pin hiện tại.

class Phone:
        def __init__(self, chip = "Snap dragon", battery_level = 100 ):
                self.__chip = chip
                self.__battery_level = battery_level

        def use_app(self, hours):
                for i in range(hours):
                        self.__battery_level -= 10
                        if self.__battery_level <= 0:
                                self.__battery_level = 0
                                break

        def charge_phone(self, hours):
                for i in range(hours):
                        self.__battery_level += 20
                        if self.__battery_level >= 100:
                                self.__battery_level = 100
                                break
        
        def display_battery(self):
                print(f"Battery percentage: {self.__battery_level}%")


phone = Phone()
result =  phone.use_app(7)
phone.display_battery()
phone.charge_phone(2)
phone.display_battery()

class Samsung(Phone):
        def __init__(self, color, chip="Snap dragon", battery_level=100):
                super().__init__(chip, battery_level)
                self.colora = color

s1 = Samsung("Black")
print(s1.colora)