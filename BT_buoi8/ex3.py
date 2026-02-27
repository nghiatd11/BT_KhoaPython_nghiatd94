# Bài 3: Automation - LoginPage Object Tạo một class LoginPage hoàn chỉnh (không cần chạy Selenium thật, chỉ cần viết code).
# __init__(self, driver): Lưu lại driver.
# Thuộc tính: username_locator, password_locator, login_button_locator.
# Phương thức enter_username(self, username): Giả lập việc tìm element username và gõ username vào. Dùng print() để mô phỏng.
# Phương thức enter_password(self, password): Tương tự cho password.
# Phương thức click_login(self): Tương tự cho nút login.
# Phương thức login(self, username, password): Gọi 3 phương thức trên theo đúng thứ tự để thực hiện toàn bộ quy trình đăng nhập.
driver = "Driver"
class Login_page:
        def __init__(self, driver):
                self.driver = driver
                self.username_locator = "###username_locator"
                self.password_locator = "###password_locator"
                self.login_button_locator = "###login_button_locator"

        def enter_username(self, username):
                print(f"navigate to {self.username_locator}")
                print(f"enter username {username}")

        def enter_password(self, password):
                print(f"navigate to {self.password_locator}")
                print(f"enter username {password}")

        def click_button_login(self, etc=""):
                print(f"click {self.login_button_locator}")
                
        def login(self, username, password):
                self.enter_username(username)
                self.enter_password(password)
                self.click_button_login()

user1 = Login_page(driver)
user1.login("nghiatd94", "abc123")

