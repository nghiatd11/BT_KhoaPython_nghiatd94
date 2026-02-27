# Bài 1: Lớp Product (Sản phẩm) Viết một class Product để quản lý thông tin sản phẩm.
# __init__: Nhận vào name, price, và quantity (số lượng).
# Phương thức get_total_price(): Trả về tổng giá trị của sản phẩm đó (price * quantity).
# Phương thức display_info(): In ra thông tin sản phẩm theo định dạng: 
# "Sản phẩm: [Tên], Đơn giá: [Giá], Số lượng: [Số lượng], Tổng giá trị: [Tổng giá trị]".

class Product:
            def __init__(self, name, price, quantity):
                self.name = name
                self.price = price
                self.quantity = quantity

            def get_total_price(self):
                return self.price * self.quantity
            
            def display_info(self):
                total_price = self.get_total_price()
                print(f"Sản phẩm: {self.name}, Đơn giá: {self.price}, Số lượng: {self.quantity}, Tổng giá trị: {total_price} vnđ")

but_chi = Product("but  chi", 5000, 7)
but_chi.display_info()





