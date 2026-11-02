# # exercise 1
# def apply_to_all(numbers:list, action):
#     result = []
#     for n in numbers:
#         result.append(action(n))
#     return result

# def double(n):
#     return n * 2

# def round_fun(n):
#     return round(n)

# print(apply_to_all([1,2,3], double))
# print(apply_to_all([1,2,3], lambda n: n * n))
# print(apply_to_all([1.6,2.4],round_fun))
# 
# 
# 
# # exercise 2
# prices = [20,75,120,45,90]
# expensive = list(filter(lambda p: p > 50, prices))
# raised = list(map(lambda p: p + 10, prices))
# print(expensive)
# print(raised)
# 
# 
# 
# # exercise 3
# words = ["banana", "fig", "cherry", "kiwi"]
# students = [("Dana", 92), ("Avi", 78), ("Noa", 85)]

# print(sorted(words, key=len))
# print(max(words, key=len))
# best_student = max(students, key=lambda stu: stu[1])
# print(best_student)