# Bài tập thực hành phần 2 Mở rộng class BankAccount ở buổi trước. Chuyển self.balance thành self.__balance (private). 
# Đảm bảo rằng việc gửi và rút tiền chỉ có thể thực hiện thông qua các phương thức deposit() và withdraw(). 
# Trong withdraw(), thêm logic kiểm tra nếu số tiền rút lớn hơn số dư thì raise ValueError("Số dư không đủ!").

class BankAccount:
        def __init__(self, customer, balance=0):
                self.customer = customer
                self.__balance = balance

        def deposit(self, amount):
                if amount <= 0:
                        print(f"số tiền gửi không hợp lệ")
                else:
                        self.__balance += amount
                        print(f"{self.customer} đã gửi {amount} vnd")

        def display_balance(self):
                print(f"Số dư hiện tại là : {self.__balance}")

        def withdraw(self, amount):
                if amount <= 0:
                        return
                elif amount > self.__balance:
                        print(f"Số dư ko đủ để rút tiền!")
                else:
                        self.__balance -= amount
                        print(f"{self.customer} đã rút {amount} vnd")
                
                
user1 = BankAccount("TanTan", 10000)
user1.deposit(5000)
user1.display_balance()

user1.withdraw(70000)
user1.display_balance()

                
