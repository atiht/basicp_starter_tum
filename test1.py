"""
x = int (input("your distance :"))
if x >= 500 :
    print("price = 45")
    vat = 35*7/100
    print('vat = ',vat)
    print('total = ',vat +  45)
elif 500 >= x and x >= 301 :
    print("price = 35")
    vat = 35*7/100
    print('vat = ',vat)
    print('total = ',vat +  35)
elif 300 >= x and x >= 101 :
    print("price = 25")
    vat = 25*7/100
    print('vat = ',vat)
    print('total = ',vat +  25)
elif 100 >= x and x >= 51 :
    print("price = 15")
    vat = 15*7/100
    print('vat = ',vat)
    print('total = ',vat +  15)
elif 50 >= x and x >= 5 :
    print("price = 10")
    vat = 10*7/100
    print('vat = ',vat)
    print('total = ',vat +  10)
else :
    print("ส่งฟรี")
"""

"""
x = int(input("num x:"))
y = int(input("num y:"))
if x > y :
    print("x > y")
elif x < y :
    print("x < y")
elif x == y :
    print("x = y")
else :
    print("idk")
"""
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
""" 

i = 1
while i <= 100:
    print(i)
    i = i+1