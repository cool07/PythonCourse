# Task 4.2
# Составить программу, которая будет считывать введённое пятизначное число. После чего, каждую цифру этого числа
# необходимо вывести в новой строке:
# Число: 10819
# 1 цифра равна 1
# 2 цифра равна 0
# 3 цифра равна 8
# 4 цифра равна 1
# 5 цифра равна 9

def parse_number():
    number = input("Введите пятизначное число : ")
    counter = 0
    for item in number:
        counter += 1
        print (f"{counter} цифра равна {item}")

parse_number()
