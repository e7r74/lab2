# print("#1 Ratio ")
# n = int(input("n: "))
# a = n // 1000
# b = (n // 100) % 10
# c = (n // 10) % 10
# d = n % 10
#
# if a + d == b - c:
#     print("yes")
# else:
#     print("no")
#     print (" ")

# print("#2 Roskomnadzor ")
# user=int(input("user"))
# if user>=18:
#     print("Access is allowed ")
# else:
#     print("Access denied ")
#     print(" ")

#     print("#3 Arithmetic progression ")
#     n1=int(input())
#     n2=int(input())
#     n3=int(input())
#     s=n2-n1
#     e=n3-n2
#     if s==e:
#         print ("Yes")
#     else:
#         print("No")
#         print(" ")

# print("#4 Rook Move ")
# column1 = int(input())
# row1 = int(input())
# column2 = int(input())
# row2 = int(input())
# if abs(column1 - column2) == abs(row1 - row2):
#     print("no")
# else:
#     print("yes")
# print(" ")

# print("#5 King's Move ")
# column1 = int(input())
# row1 = int(input())
# column2 = int(input())
# row2 = int(input())
#
# if abs(column1 - column2) <= 1 and abs(row1 - row2) <= 1:
#     print("yes")
# else:
#     print("no")
# print ("")

# print ("#6 Average number ")
# num1=int(input("num1:"))
# num2=int(input("num2:"))
# num3=int(input("num3:"))
# result=(num1+num2+num3)/3
# print (result)
#
# print(" ")

# print("#7 Number of days ")
# month_number = int(input("Введите серийный номер месяца: "))
# if (month_number == 2):
#  print("В этом месяце 28 дней. ")
# elif (month_number <= 7 or month_number > 8):
#  print("В этом месяце 31 день. ")
# else:
#  print("В этом месяце 30 дней.")

# print ("#8 Weigh-in ceremony ")
# kg =float(input("kg:"))
# if kg<=60:
#     print("Light weight")
# elif 60<kg<65:
#     print ("First welterweight")
# elif 65<=kg<70:
#     print ("Welterweight ")

#print ("#9 Password ")
# password = input()
# coppassword = input()
# if password == coppassword:
#     print("Пароль принят ")
# else:
#     print("Пароль не принят")
# print("#10 Even or odd? ")
# number=int(input("number: "))
# if number%2==0:
#     print("even")
# else:
#     print("odd")
#
# print("#11 The smallest of two numbers ")
# number1=int(input("number1: "))
# number2=int(input("number2: "))
# if number1>number2:
#     print(number1)
# else:
#     print(number2)
# print("#12 Age Group ")
# age=int(input("age: "))
# if age<=13:
#     print("childhood")
# elif 13<age<=24:
#     print ("youth")
# elif 24<age<=59:
#     print(" maturity")
# elif 59<age:
#     print(" old")
print("#13 Triangle view ")
a, b, c = int(input()), int(input()), int(input())
sides = sorted([a, b, c])
if sides[0] == sides[1] == sides[2]:
    print("Equilateral")
elif sides[0] == sides[1] or sides[1] == sides[2]:
    print("Isosceles")
else:
    print("Versatile")