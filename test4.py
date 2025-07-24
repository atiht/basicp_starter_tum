monster = ("tum")
HP = 100
sword = 15
bow = 5
axe = 10

i = 1
disition = int(input("press 1 = qiutgame prass 2 = continue :"))
if disition == 2 :
    times = int(input("times to hit:"))
    for i in range(1, times + 1):
       weaponType =  input("select: sword, bow, axe : ")  
       if weaponType == "bow" :
            print("damage hit",bow)  
            HP = HP - bow
            print("HP BOOS",HP)
       elif weaponType == 'axe':
            print("damage hit", axe)
            HP = HP - axe
            print("HP BOOS",HP)
       elif weaponType == 'sword':
            print("damage hit ", sword)
            HP = HP - sword
            print("HP BOOS",HP)
    if HP == 0 :
        print("BOSS DEAD")
    elif HP < 0 :
        HP == 20 
        print("HP BOSS 20")
    elif HP > 0 :
        print("player dead")
else:
    print("you lose")
        



