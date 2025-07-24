def grade(score):
    if score >=50:
        print("you pass")
        if score >=80:
            print("Grade A")
        elif score >=70:
            print("Grade B")
        elif score >=60:
            print("Grade C")
        else:
            print("Grade D")
    else :
        print("Grade F")
        print("you fail")

score1 = int(input("your score1 :"))
grade(score1)
score2 = int(input("your score2 :"))
grade(score2)
score3 = int(input("your score3 :"))
grade(score3)
    