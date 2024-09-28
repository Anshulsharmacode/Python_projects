print("Table for multification")

num = int(input("Enter the number "))

for i in range(1,11) :
    if i==5:
        continue
    print(num , "x", i ,"=",(num*i))

