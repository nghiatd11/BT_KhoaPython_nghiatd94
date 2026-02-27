# 5. Tạo set emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}.
# Quan sát kết quả khi in set ra.
# Thêm "c@gmail.com".
# Thử xóa "d@gmail.com" bằng remove và bằng discard, giải thích sự khác nhau.

emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
# emails = ("a@gmail.com", "b@gmail.com", "a@gmail.com")
print(emails)
emails.add("ccc@gmail.com")
print(emails)
emails.remove("a@gmail.com")
print(emails)
emails.remove("a@gmail.com")
# emails.discard("DDDDDD@gmail.com")
print(emails)

# Với kiểu dữ liệu set thì dùng .remove() để xóa giá trị tồn tại, nếu ko tồn tại sẽ lỗi KeyError
# còn .discard() thì có thể xóa cả giá trị không tồn tại mà ko gây lỗi gì