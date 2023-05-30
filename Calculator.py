def main():

    print("==========Simple Calculator==========")
    Num1 = float(input("Masukkan angka pertama: "))
    Num2 = float(input("Masukkan angka kedua: "))
    varOp = input("Masukkan operator (+, -, *, /, %): ")

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
        print("Input operator salah!")

    restart = input("Apakah anda ingin menggunakan Kalkulatornya lagi? (Y/N)")
    if restart == 'Y':
        main()
    elif restart == 'N':
        exit()
    else:
        print("Y/N")

main()