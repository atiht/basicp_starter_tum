
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




