# 6. Bài tập tổng hợp cuối buổi
# Bài 1: Nhập số
# Viết chương trình yêu cầu người dùng nhập số.
# Nếu nhập đúng → in bình phương.
# Nếu nhập sai → in "Sai định dạng".
try:    
        a = int(input("Hãy nhập 1 số: "))
except (ValueError) as e:
        print(f"Sai định dạng số: {e}")
else:
        print(f"Bình phương = :  {a**2}")
#____________________________________________________


