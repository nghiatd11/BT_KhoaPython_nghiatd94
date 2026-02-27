# Bài tập thực hành phần 2.3
# Đọc file linh hoạt: Viết code để mở và đọc một file có tên do người dùng nhập.
# Dùng một khối except duy nhất để bắt cả hai lỗi FileNotFoundError (file không tồn tại) 
# và  PermissionError (không có quyền đọc file).


try:
        with open("daata.txt", "r") as file:
                data = file.read()
                print(f"Noi dung File Data: \n{ data}" )
except (FileNotFoundError, FileExistsError, PermissionError) as e:
                print(f"Loi {e}")
