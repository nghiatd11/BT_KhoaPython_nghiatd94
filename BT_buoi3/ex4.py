# 3. Phân loại học lực theo điểm trong list sau
# scores = [95, 82, 67, 45, 88, 90, 50]
# Từ 90 điểm trở lên -> xuất sắc
# => 70: Khá
# => 50: trung bình
# < 50 : Yếu

scores = [95, 82, 67, 45, 88, 90, 50]

for score in scores:
    if score > 90:
        print("Xuất sắc")
    elif score >= 70:
        print("Khá")
    elif score >= 50:
        print("Trung Bình")
    else:
        print("Yếu")