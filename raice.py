# def parse_percentage(text):
#     if not text.endswith("%"):
#         raise ValueError("must end with %")
#     try:
#         number = int(text[:-1])
#     except ValueError as error:
#         return f"The number must be int, {error}"
# 
#     if number < 0 or number > 100:
#         raise ValueError("the number must be between 0-100")
#     return number
# 
# print(parse_percentage("75%"))
# print(parse_percentage("101%"))
# print(parse_percentage("75"))
# 
# # exercise 1
# MAX_AGE = 120
# MIN_AGE = 0
# 
# def set_age(age):
#     if age <= MAX_AGE and age >= MIN_AGE:
#         return "ok"
#     else:
#         return f"error: age must be between 0 and 120, got"
# 
# def is_a_normal_age(age):
#     status = set_age(age)
#     if status is not "ok":
#         raise ValueError("error: age must be between 0 and 120, got {age}")
# 
# def check_ages(ages:list):
#     for age in ages:
#         status = set_age(age)
#         print(f"{status}: {age}")
# 
# check_ages([1,121,50])
# 
# # exercise 2
# 
# def validate_username(name):
#     if len(name) < 3:
#         raise ValueError("too short")
#     elif " " in name:
#         raise ValueError("no spaces allowed")
#     else:
#         return name
# 
# def is_valid(names:list):
#     for name in names:
#         try:
#             print("valid:", validate_username(name))
#         except ValueError as error:
#             print(name, "->", error)
# 
# is_valid(["dana", "al", "big boss"])
# 
# 
## exercise 3
# 
# def apply_discount(price, percent):
#     if price < 0:
#         raise ValueError("price cannot be negative")
#     return price * percent
# 
# def repoort_price(price):
#     try:
#         total = apply_discount(price, 0.90)
#         print(total)
#     except ValueError as error:
#         print("error: {error}")
# 
# def price_or_zero(price):
#     try:
#         total = apply_discount(price, 0.90)
#         print(total)
#     except ValueError:
#         print(0)
