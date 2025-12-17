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


# pr 1
# score = int(input("Please enter you score: "))
# print(score)
# print(type(score))
# gender = "m"
#
# if score < 0:
#     print("Invalid - Negative number")#
#     if gender == "m":
#         print("sir")
# elif score < 50:
#     print("fail")
# elif score < 100:
#     print("pass")
# else:
#     print("Invalid - out of range")

 # pr 2
## 1. Ask for age and convert to integer
age = int(input("Please enter your age: "))

# 2. Check categories using if/elif/else
if age < 5:
    print("Free entry")

elif age <= 17:
    # This runs only if age is >= 5 AND <= 17
    print("Child ticket")

elif age <= 64:
    # This runs only if age is >= 18 AND <= 64
    print("Adult ticket")

else:
    # This runs for anyone 65 or older
    print("Senior ticket")
#
#











