#List

students = ["Tung", "Quan", "Tuan", "Mai"]
print(students)
students.append("Hung")         # them vao cuoi danh sach
students.insert(1, "Ngoc")      #them vao vi tri bat ki` trong DSach
students.remove("Hung")         # Xoa 1 phần tử trong danh sách theo kiểu truyền giá trị
students.pop(1)            # xóa 1 phần tử trong danh sách truyền index or Key
print(students)


# Đếm Count và in ra số lượng testcase pass/fail
results = ["Pass", "Fail", "Pass", "Fail", "Pass"]
print(f"day la kqua:", results)
print(f"Tong so case Pass", results.count("Pass"))
results.append("Fail")
print(f"Tong so case Fail", results.count("Fail"))

#Tình trung bình cộng và min max dãy số trong List
scores = [4, 5, 6, 7, 8.8]
print(f"Trung binh cong: {sum(scores)/len(scores)}")
print("Trung binh cong: ".format((sum(scores)/len(scores))))