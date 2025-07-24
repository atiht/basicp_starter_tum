"""
x = int (input("your score :"))
if x >= 80 :
    print("A")
elif 79 >= x and x >= 70 :
    print("B")
elif 69 >= x and x >= 60 :
    print("C")
elif 59 >= x and x >= 50 :
    print("D")
else :
    print("F") 
"""
"""
x = int (input("your score :"))
if x >= 50 :
    print("ผ่าน")
    if x >= 80 :
        print("A")
    elif  x >= 70 :
        print("B")
    elif x >= 60  :
        print("C")
    else :
        print("D") 
"""
"""
num = int(input("Enter number :"))
sum = 0
for i in range(1,num+1):
    sum = sum + 5
    print(f"ครั้งที่{i}=",sum)
"""

"""
sum = 1
num = int(input("Enter number :"))
thimes = int(input("Enter times :"))
while sum <= thimes:
    print(num)
    num += 5
    sum += 1
"""

member = input("Enter your member :")
cost = int(input("เงินรวมที่สั่งอาหาร"))
date = int(input("วันที่สั่ง"))
sale = (cost*15/100)
cost_member_Gold_1000up = (cost-sale)

if   member == "Gold" :
    if cost >= 1000 :
        print(cost)
        print("ได้รับส่วนลด15%")
        print(cost_member_Gold_1000up)
    else :
        print("ได้รับส่วนลด 10%")
if member == "Silver" :
    if cost >= 1000 :
        print("ได้รับส่วนลด 10%")
    else :
        print("ได้รับส่วนลด 5%")
if member == "ไม่มีสมาชิก" :
    print("ไม่มีส่วนลดจ้า")

if date % 2 == 1 :
    print("ยินดีด้วย คุณได้บส่วนลด 5%")
elif date % 2 == 0 :
    print("คุณไม่ได้รับส่วนลด มาสั่งพรุ่งนะ")
elif date > "31" :
    print("บ้านพ่องมีวันที่เกิน 31 หรอ")