# # exercise 3

# def to_celsius(fahrenheit):
#     return ((fahrenheit - 32) * 5) / 9
# print(to_celsius(212))
# print(to_celsius(32))


# exercise 4
# age = 25
# print("Age: " + age)
# שגיאת typeError מכיון שלא ניתן לחבר str ל int
# פתרונות:

# age = 25
# print(f"Age: {age}")
# 
# age = "25"
# print("Age: " + age)


# exercise 5
# def average(numbers):
#     if not numbers:
#         return 0
#     return sum(numbers) / len(numbers)
# print(average([80, 90]))
# print(average([]))