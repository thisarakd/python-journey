num = int(input("Enter a number : "))

if num >= 0:
    if num % 2 == 0:
        print(f'{num} is a positive and even number')
    else:
        print(f'{num} is a positive and odd number')
else:
    if num % 2 == 0:
        print(f'{num} is a negative and even number')
    else:
        print(f'{num} is a negative and odd number')