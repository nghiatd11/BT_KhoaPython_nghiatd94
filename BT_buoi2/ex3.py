# 3. Khai báo biến sau:                                                                                                                                                                                                                                                                                                                                                                                      
a = 10                                                                                                                                                                                                        
b = 3.5                                                                                                                                                                                                        
c = True                                                                                                                                                                                                        
d = None                                                                                                                                                                                                        
e = "Python"                                                                                                                                                                                                                                                                                                                                                                                                      
# In ra kiểu dữ liệu của từng biến (type()).    
print(f"Type a : {type(a)}")
print(f"Type b : {type(b)}")
print(f"Type c : {type(c)}")
print(f"Type d : {type(d)}")
print(f"Type e : {type(e)} \n")
                                                                                                                                                                                                                                                                                                                                                                                         
# Tạo list scores = [9, 7, 10, 8, 6] và làm:                                                                                                                                                                                                                                                                                                                                                                                                      
# In ra điểm cao nhất.                                                                                                                                                                                                                                                                                                                                                                                   
# Tính điểm trung bình.                                                                                                                                                                                                                                                                                                                                                                                                 
# Thêm điểm 5 vào cuối list.             
scores = [9, 7, 10, 8, 6]    
print(f"max score =  {max(scores)}")             
print(f"average score =  { (sum(scores)  /  len(scores)) }")             


                                                                                                                                                                              
# Tạo tuple birthday = (11, 9, 2025) → in ra ngày, tháng, năm.                                                                                                                                                                                                        
# Thử thay đổi giá trị trong tuple và quan sát lỗi.      
# 
birthday = (11, 9, 2025) 
day = birthday[0]
month = birthday[1]
year = birthday[2]
# birthday[2] = 2027

print(day, month, year)