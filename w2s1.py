# print("Enter your name: ")
# name = input()
#
# print("Welcome, " + name)
# print("Welcome, " + name.strip().upper().replace("A", "X"))
#
# print("Enter your age: ")
# age =  int(input())
# print(f"You are {age} years old")
#
# print(f"In ten years you will be {age + 10} years old")
#

score = int(input("Please enter you score: "))
print(score)
print(type(score))
gender = "m"

if score < 0:
    print("Invalid - Negative number")#
    if gender == "m":
        print("sir")
elif score < 50:
    print("fail")
elif score < 100:
    print("pass")
else:
    print("Invalid - out of range")













