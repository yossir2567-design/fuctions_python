# # exercise 1
# def to_number(text):
#     try:
#         val = int(text)
#     except ValueError as e:
#         val = f"{text} is not a number {e}"
#     return val

# exercise 2
# def safe_divide(text1, text2):
#     try:
#         int(text1) and int(text2)
#     except ValueError as e:
#         print(f"numbers only {e}")
# 
#     try:
#         return text1 / text2
#     except ZeroDivisionError as e:
#         print(f"cannot divide by zero {e}")
# 
# 
# exercise 4
def pick(names:list, position_text:str):
    try:
        val = int(position_text) - 1
    except ValueError:
        return "not a number"
    try:
        return names[val]
    except IndexError as e:
        return f"no such position :{e}"

print(pick(["Dana", "Avi", "Noa"], "9"))
    