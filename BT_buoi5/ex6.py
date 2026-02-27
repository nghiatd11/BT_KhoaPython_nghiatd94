# Bài 4: Automation
# Giả lập tìm element "submit".
# Nếu không tìm thấy → in "Không tìm thấy element".
# Luôn in "Đóng trình duyệt".

element = "submit"
try:
        print("Tìm element Submit")
except Exception as e:
        print(e)
else:
        print("Có tìm thấy element Submit")
finally:
        print("Đóng trình duyệt")