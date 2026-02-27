
# Chúng ta cần viết chương trình Python để duyệt qua dãy số tự nhiên từ 1 đến 20. 
# Với mỗi số, chương trình sẽ kiểm tra theo điều kiện:
# 1. Nếu số chia hết cho cả 3 và 5 → in ra "FizzBuzz".
# 2. Nếu số chỉ chia hết cho 3 → in ra "Fizz".
# 3. Nếu số chỉ chia hết cho 5 → in ra "Buzz".
# 4. Nếu số không chia hết cho 3 hay 5 → in ra chính số đó.

for i in range(1, 21):
    #chia het cho 3 va 5
    if i % 3 == 0 and i % 5 ==0:
        print(f"FizzBuzz")
    elif i % 3 == 0:
        print(f"Fizz")
    elif i % 5 == 0:
        print(f"Buzz")
    elif i % 3 != 0 and i % 5 !=0:
        print(f"So ko chia het cho 3 va 5: {i}")