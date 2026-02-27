# Bài 3: File
# Đọc file data.txt.
# Nếu file tồn tại → in nội dung.
# Nếu không → in "File không tồn tại".
# Luôn in "Kết thúc chương trình".

try:
        with open("dataa.txt", "r", encoding="utf-8") as file:
                data = file.read()
except (FileNotFoundError, FileExistsError) as e:
        print(f"File không tồn tại: {type(e).__name__}")
else:
        print(f"Nội dung file: {data}")
finally:
        print("Kết thúc chương trình")
