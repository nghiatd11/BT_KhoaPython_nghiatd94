# Bài 4: Tính Trừu tượng (Abstraction) - Thanh toán Online
# Ý tưởng: Mọi cổng thanh toán đều bắt buộc phải có chức năng "Thanh toán"
# . Nhưng cách "Momo" thanh toán (quét mã QR) sẽ khác cách "Thẻ tín dụng" thanh toán (nhập số thẻ).
# Đề bài:
# Sử dụng module abc, tạo một lớp trừu tượng PaymentGateway.
# Trong lớp này, định nghĩa một phương thức trừu tượng là process_payment(self, amount).
# Tạo lớp con MomoPayment(PaymentGateway):
# Triển khai phương thức process_payment(self, amount) 
# ----để in ra: "Đang xử lý thanh toán Momo số tiền [số tiền]... Vui lòng quét mã QR."

# Tạo lớp con CreditCardPayment(PaymentGateway):
# Triển khai phương thức process_payment(self, amount) 
# -------để in ra: "Đang xử lý thanh toán thẻ tín dụng số tiền [số tiền]... Vui lòng nhập thông tin thẻ."

from abc import ABC, abstractmethod
class PaymentGateway(ABC):
        @abstractmethod
        def process_payment(self, amount):
                print("Hãy chọn phương thức thanh toán")

class Momo(PaymentGateway):
        # pass
        def process_payment(self, amount):
                print(f"Đang xử lý thanh toán Momo số tiền {amount} Vui lòng quét mã QR")

class CreditCard(PaymentGateway):
        def process_payment(self, amount):
                print(f"Đang xử lý thanh toán thẻ tín dụng số tiền {amount} Vui lòng nhập thông tin thẻ")

momo = Momo()
momo.process_payment(50000)
credit = CreditCard()
credit.process_payment(50000)