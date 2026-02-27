# Bài tập thực hành phần 2.2
# Tính toán an toàn: Viết chương trình chia 2 số a và b do người dùng nhập.
# Dùng try-except riêng biệt để bắt lỗi ValueError (nếu nhập chữ) 
# và ZeroDivisionError (nếu chia cho 0) với các thông báo lỗi tương ứng
def twoNumbersDivison():
        try:
                a = int(input("Nhap so a: "))
                b = int(input("Nhap so b: "))
                print(f"a : b = {a / b}")

        # except ValueError:
        #         print("Người dùng nhập số không hợp lệ!")
        # except ZeroDivisionError:
        #         print("Lỗi chia cho 0.")
                
        except (ValueError, ZeroDivisionError ) as e:
                print(f"Bắt 2 lỗi ValueError và lỗi ZeroDivison:: {type(e).__name__}")

        except Exception as e:
                print(f"Loi ko xac dinh: {e}")

twoNumbersDivison()
