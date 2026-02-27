# Bài 2: Máy tính an toàn
# Viết hàm safe_divide(a, b) chia 2 số.
# Nếu b = 0 → trả về "Không thể chia cho 0".
# Ngược lại → trả về kết quả.
def safe_divide():
        try:
                a = int(input("Nhập số a: "))
                b = int(input("Nhập số b: "))
                c = a / b
        except ZeroDivisionError as e:
                print(f"Không thể chia cho 0: {e}")
        else:
                print(f"Kết quả a : b  =  {c}")    
            
safe_divide()
