# đọc file login_data.xlsx
import openpyxl as xl
import json
import os
data_path = os.path.join( "..", "data", "login_data.xlsx")
json_path = os.path.join( "..", "data", "users.json")
try:
        book = xl.load_workbook(data_path)
        sheet1 = book.active

        headers = [cell.value for cell in sheet1[1]]
        users = []
        for row in sheet1.iter_rows(min_row= 2 , values_only=True):
            user = {}
            for header, row_value in zip(headers, row):
                    user[header] = row_value
            users.append(user)
        # print(f"Danh sach Users Json \n{users}")

        with open(json_path, "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4, ensure_ascii=False)
        with open(json_path, "r", encoding="utf-8") as file:
               data_user = json.load(file)
               print(f"Data User: \n{data_user}")

except FileNotFoundError as e:
        print(f"Khong tim` thay file {e}")
except FileExistsError as e:
        print(f"File khong ton` tai {e}")
else:
        print("Mo va ghi file thanh cong")
        



