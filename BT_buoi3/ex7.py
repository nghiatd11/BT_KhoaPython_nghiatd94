# 2. Cho list số sau
numbers = [2, 5, 8, 11, 14, 17, 20]

# In ra tất cả số trong list.
for number in numbers:
    print(f"Số {number}")
print()

# In ra số chẵn trong list.
for number in numbers:
    if number % 2 == 0:
        print(f"Các số chẵn trong list là: {number}")
print()

# Tính tổng tất cả số trong list.
print(f"Tổng bằng: {sum(numbers)}")
print()

# In ra bảng cửu chương của từng số trong list (gợi ý: dùng for i in range(1, 11):)
#  (bài tập nâng cao dùng for trong for, có thể làm hoặc không)
for number in numbers:
    print(f"Bảng Cửu Chương của {number}")
    for x in range(1, 11):
        print(f"  {number} x {x} = {number*x}")
    


