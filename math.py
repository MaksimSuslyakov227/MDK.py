a = int(input('Введите число от 1000 до 9999')
        if 1000 < a > 9999:
            print('Попробуйте ещё раз')
            return
        else:
            if (a % 47 == 43) and (a % 43 == 37):
                print("Число подходит")
            else:
                print("Число не подходит")
                return
