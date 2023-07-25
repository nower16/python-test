def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(30,4,6))

num1 = float(input("Enter first number:"))
operator = input("Enter operator(+, -, *,/,%) :")
num2 = float(input("Enter the second number:"))

if operator == '+':
    print(num1+num2)
elif operator == '-':
    print(num1-num2)
elif operator == '*':
    print(num1*num2)
elif operator == '/':
    print(num1/num2)
elif operator == '%':
    print(num1%num2)
else:
    print('Invalid num')


