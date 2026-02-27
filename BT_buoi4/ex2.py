# Chuẩn hóa số điện thoại: Một SĐT được nhập vào có dạng messy_phone = " 090-123 4567 ".
#  Hãy viết code để chuẩn hóa SĐT này về dạng 0901234567 (loại bỏ hết khoảng trắng và gạch nối).

messy_phone = " 090-123 4567 "
clean_phone = messy_phone.strip().replace("-","").replace(" ","")
print(clean_phone)
