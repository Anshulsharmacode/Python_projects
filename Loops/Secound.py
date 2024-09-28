n =int(input("enter the number "))

result=0

for i in range (0,n+1):
    if i%2 ==0:
        result += 1

print("the even number is ", result)