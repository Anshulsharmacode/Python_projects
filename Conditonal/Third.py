print("grade calculator")

Grade= int(input("enter the grade for cheking"))

if Grade >= 101:
    print("enter a valid grade")
    exit()

if Grade > 90:
    print("you are getting A")

elif Grade > 80:
    print("you are getting B")

elif Grade > 70:
    print("you are getting C")

elif Grade > 60:
    print("you are getting D")

else :
    print("you are getting F")