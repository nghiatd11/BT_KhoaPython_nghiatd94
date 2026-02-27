# 1. Kiểm trả message đăng nhập xem có nằm trong danh sách expected
# expected_messages = ["Login successfull", "Welcome"]
# actual_message = "Welcome"
# 1.1 Nếu actual message ằm trong expected_messages thì in ra "Message hop le" 
# ngược lại thì in ra "Message khong hop le"


expected_messages = ["Login successfull", "Welcome"]
actual_message = "Welcome"

if actual_message in expected_messages:
    print("Message Hop Le")
else:
    print("Message Khong Hop Le")