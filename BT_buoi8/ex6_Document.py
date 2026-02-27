# Bài 2: Tính Kế thừa (Inheritance) - Các loại Tài liệu
# Ý tưởng: Mọi tài liệu đều có một "tiêu đề", nhưng mỗi loại tài liệu lại có nội dung khác nhau. 
# -----"Bài báo" và "Email" sẽ cùng kế thừa đặc điểm chung từ "Tài liệu".
# Đề bài:
# Tạo một lớp cha Document có:
# __init__(self, title): Để lưu lại tiêu đề.
# Phương thức show_info(self): In ra "Tiêu đề: [tên tiêu đề]".
# Tạo lớp con Article(Document) kế thừa từ Document:
# __init__(self, title, author): Gọi __init__ của lớp cha để lưu title, và lưu thêm author.
# Viết lại (override) phương thức show_info(self) để in ra: "Bài báo: [tên tiêu đề] - Tác giả: [tên tác giả]".
# Tạo lớp con Email(Document) kế thừa từ Document:
# __init__(self, title, sender): Gọi __init__ của lớp cha để lưu title, và lưu thêm sender.
# Viết lại (override) phương thức show_info(self) để in ra: f"Email: [tên tiêu đề] - Người gửi: [tên người gửi]".
# Mục tiêu: Hiểu cách lớp con thừa hưởng và mở rộng (hoặc thay đổi) hành vi của lớp cha.

class Document:
        def __init__(self, title):
                self.title = title

        def show_infor(self):
                print(f"Tiêu đề: {self.title}")

class Article(Document):
        def __init__(self, title, author):
                super().__init__(title)
                self.author = author

        def show_infor(self):
                print(f"Bài báo: {self.title} - Tác giả: {self.author}")

class Email(Document):
        def __init__(self, title, sender):
                super().__init__(title)
                self.sender = sender

        def show_infor(self, email):
                print(f"Email: {email} - Người gửi: {self.sender}")

article = Article( "Monetization", "Selby")
article.show_infor()

e1 = Email("Social life", "Toby")
e1.show_infor("toby@gmail.com")

