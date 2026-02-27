# Viết chương trình Python để:
# Đọc dữ liệu từ file students.xlsx.
# Lưu dữ liệu vào list of dict trong Python.
# Ghi dữ liệu này ra file report.json theo format JSON, giữ nguyên tiếng Việt.
import json, os
import openpyxl as xl

excel_path = os.path.join("..", "data", "students.xlsx")
json_path = os.path.join("..", "data", "students.json")

try : 
        # Mo file excel
        book = xl.load_workbook(excel_path)
        sheet = book.active
        headers = [cell.value for cell in sheet[1]]
        students = []
        for row in sheet.iter_rows(min_row=2 , values_only=True):
                student = {}
                for index, key in enumerate(headers):
                        student[key] = row[index]
                students.append(student)
        # Ghi file json
        with open(json_path, "w", encoding = "utf-8") as file:
                json.dump(students, file, indent= 4, ensure_ascii=False)
        with open(json_path, "r", encoding= "utf-8")as file:
                data = json.load(file)


except FileNotFoundError as e:
        print(f"Lỗi : Không tìm thấy File: {e}")
# except FileExistsError as e:
#         print(f"Lỗi : File: không tồn tại {e}")
        