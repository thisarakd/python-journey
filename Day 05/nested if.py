a = input("Enter 1st Number :")
b = input("Enter 2nd Number :")
c = input("Enter 3rd Number :")

if a > b:
    if a > c:
        print(f'{a} is the largest number')
    else:
        print(f'{c} is the largest number')
else:
    if b > c:
        print(f'{b} is the largest number')
    else:
        print(f'{c} is the largest number')
