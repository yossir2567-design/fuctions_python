import logging

# # exercise 1
# logging.basicConfig(
#    filename="shop.log",
#    filemode="a",
#    level=logging.INFO,
#    format="%(asctime)s %(levelname)-8s %(message)s")

# 
# def order(products, quantity):
#     if products - quantity <= 2:
#         logging.warning("Warning, Only 2 left")
#     if products - quantity < 0:
#         logging.error("Not enough in stock")
#     logging.info("The order has been confirmed.")
#     products -= quantity
# 
# 
# exercise 2
# 1. "a": add "w": write
# 2. אי אפשר לראות את תיעוד הבעיה
# 
# 
# # exercise 3
# def filter_total(numbers:list):
#     total = 0
#     for num in numbers:
#         try:
#             val = int(num)
#         except ValueError as e:
#             logging.error(f"{e}, only numbers")
#         total += val
# products = 100

# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")
# logging.basicConfig(
#     filename="log.log",
#     filemode="a",
#     level = logging.DEBUG,
#     format = "%(asctime)s %(levelname)-8s %(message)s")