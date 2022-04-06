import re
n = int(input())
phone_num = []
if n >=1 and n <= 10:
    for i in range (1, n+1):
        phone_num.append(input())
    for x in phone_num:
        if len(x) >=2 and len(x) <= 10:
            match = re.search(r"^[7-9]\d{9}",x)
            if match:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
