# Bài tập 3: Xử lý ValueError và lỗi logic với raise
# Bài toán: Viết một chương trình yêu cầu người dùng nhập vào năm sinh và tính tuổi của họ.
#  Chương trình phải xử lý được các trường hợp nhập sai.
# Yêu cầu:
# Sử dụng khối try-except để bắt lỗi ValueError nếu người dùng nhập vào chữ thay vì số.
# Sau khi chuyển đổi thành số thành công, hãy kiểm tra xem năm sinh có hợp lệ hay không 
# (ví dụ: không được lớn hơn năm hiện tại).
# Nếu năm sinh không hợp lệ, hãy dùng raise ValueError để chủ động tạo ra một lỗi với thông báo "Năm sinh không thể lớn hơn năm hiện tại."
# Sử dụng khối else để in ra tuổi của người dùng chỉ khi mọi thứ đều hợp lệ.
from datetime import datetime
try:
        a = int(input("Vui lòng nhập năm sinh: "))
        current_year = datetime.now().year
        if a > current_year:
                raise ValueError ("Năm sinh không thể lớn hơn năm hiện tại")
        elif a < 1930:
                raise ValueError ("Năm sinh không hợp lệ.")
        
        current_age = current_year - a
except ValueError as e:
        print(f"Số năm sinh không hợp lệ: {e}")
else:
        print(f"Bạn năm nay {current_age} tuổi")

# current_year = datetime.now().year
# print(current_year)


# from datetime import datetime
# def calculate_dob(a: int):
#         try:
#                 a = int(a)
#                 current_year = datetime.now().year
#                 if a > current_year:
#                         raise ValueError ("Năm sinh không thể lớn hơn năm hiện tại")
#                 elif a < 1930:
#                         raise ValueError ("Năm sinh không hợp lệ.")
                
#                 current_age = current_year - a
#         except ValueError as e:
#                 print(f"Số năm sinh không hợp lệ: {e}")
#         else:
#                 print(f"Bạn năm nay {current_age} tuổi")

#         return current_age
