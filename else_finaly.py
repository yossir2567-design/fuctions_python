# exercise 1
# def half(text):
#     try:
#         number = int(text)
#     except ValueError:
#         print("not a number", text)
#     else:
#         print("helf", number / 2)
#     finally:
#         print("checked", text)
# half("8")
# half("x")
# # helf 4.0
# # checked 8
# # not a number x
# # checked x
# 
# 
# # exercise 2
# def check(number):
#     try:
#         if number > 0:
#             return "positive"
#         return "not positive"
#     finally:
#         print("done checking", number)
# print(check(5))
# print(check(-2))
# 
# # אם יש except מתחילים מלמעלה ואם אין מתחילים מ finally
# 
# 
# 
# # exercise 3
# def parse_quantity(text):
#     try:
#         number = int(text)
#     except ValueError:
#         print(f"invalid: {text}")
#     else:
#         print(f"quantity: {number}")
#     finally:
#         print("---")
# 
# parse_quantity("3")
# parse_quantity("three")