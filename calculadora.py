num1 = float(input("Digite o primeiro número"))
num2 = float(input("Digite o segundo número"))

op = input("digite a operação\n")
if op=="+":
    res=num1 + num2
    print('{} + {}" = '.format(num1, num2))
    print(num1+num2)

if op=="*":
    res=num1 * num2

    print('{} * {}" = '.format(num1, num2))
    print(num1*num2)

if op=="-":
    res=num1 - num2

    print('{} - {}" = '.format(num1, num2))
    print(num1-num2)

if op=="/":
    if num2 == 0:
        print("não é possivel dividir por zero")
    else:
        res=num1 / num2

    print('{} / {}" = '.format(num1, num2))
    print(num1/num2)