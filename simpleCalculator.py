def main():

    print("==========Simple Calculator==========")
    Num1 = float(input("Input the first number: "))
    Num2 = float(input("Input the second number: "))
    varOp = input("Input the Operator (+, -, *, /, %): ")

    if varOp == '+':
        result = Num1 + Num2
        print(result)
    elif varOp == '-':
        result = Num1 - Num2
        print(result)
    elif varOp == '*':
        result = Num1 * Num2
        print(result)
    elif varOp == '/':
        result = Num1 / Num2
        print(result)
    elif varOp == '%':
        result = Num1 % Num2
        print(result)
    else:
        print("Wrong operator!")

    restart = input("Do you want to use this Calculator Again? (Y/N)")
    if restart == 'Y':
        main()
    elif restart == 'N':
        exit()
    else:
        print("You can only type (Y/N)")

main()
