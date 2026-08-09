         #Taking user input:-
#Example: Normal input
input("Apna name bata:")

#Example: Adding two number(not worknig coz there is no type conversion).
First_num = input("Enter first num:")
Second_num =input("Enter second num:")
result = First_num + Second_num
print(result)

         #Type Conversion:-
#Two types:
#1 Implicit
#2 Explicit

#Explicit example: Adding two number(worknig coz there is a type conversion called int).
First_num = int(input("Enter first num:"))
Second_num = int(input("Enter second num:"))
result = First_num + Second_num
print("Answer:",end = ' ')
print(result)
