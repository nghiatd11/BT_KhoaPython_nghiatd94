# 4. Tạo dictionary student = {"name": "Lan", "age": 18, "email": "lan@gmail.com"}.

# In ra tên và email.
student = {"name": "Lan", "age": 18, "email": "lan@gmail.com"}

for key in student:
        if key == "age":
                continue
        print(f"{key} : {student[key]}")