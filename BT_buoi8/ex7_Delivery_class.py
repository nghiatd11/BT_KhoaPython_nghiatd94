# Bài 3: Tính Đa hình (Polymorphism) - Giao hàng
# Ý tưởng: Có nhiều phương thức giao hàng khác nhau (Xe máy, Xe tải). 
# ----Cùng một hành động là calculate_fee (tính phí), nhưng mỗi phương thức lại có cách tính riêng.
# Đề bài:
# Tạo 3 class riêng biệt: MotorbikeDelivery, GrabDelivery, và TruckDelivery.
# Mỗi class đều có một phương thức tên là calculate_fee(self, distance_km):
# MotorbikeDelivery: Phí là distance_km * 5000.
# GrabDelivery: Phí là distance_km * 7000.
# TruckDelivery: Phí là distance_km * 20000.
# Viết một hàm bên ngoài các class tên là get_shipping_cost(delivery_method, distance):
# Hàm này nhận vào một đối tượng phương thức giao hàng và một quãng đường.
# Bên trong, nó sẽ gọi phương thức calculate_fee của đối tượng đó và in ra kết quả.
# Mục tiêu: Thấy được rằng hàm get_shipping_cost có thể hoạt động với bất kỳ đối tượng giao hàng nào
# , miễn là đối tượng đó có phương thức calculate_fee.


class MotorbikeDelivery:
        def calculate_fee(self, distance_km):
            return distance_km * 5000
        
class GrabDelivery:
        def calculate_fee(self, distance_km):
            return distance_km * 7000
        
class TruckDelivery:
        def calculate_fee(self, distance_km):
            return distance_km * 20000
        
def get_shipping_cost(delivery_method, distance, provider_name):
        shipping_cost = delivery_method.calculate_fee(distance)
        print(f"Shipping cost: {shipping_cost} for {provider_name}")

moto = MotorbikeDelivery()
grab = GrabDelivery()
truck = TruckDelivery()

get_shipping_cost(moto, 3, "MotoBike")
get_shipping_cost(grab, 5, "Grabbike")
get_shipping_cost(truck, 4, "Truck")




