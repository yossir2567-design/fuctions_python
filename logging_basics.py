import logging
# exercise 1
# steps = {"DEBUG": "level_1",
#          "INFO": "level_2",
#          "WARNING": "level_3",
#          "ERROR": "level_4",
#          "CRITICAL": "level_5"
#        }
# 
# 

# # exercise 2
# # if we want to see evryshing:
# logging.basicConfig(level=logging.DEBUG)
# 
# 
# 
# exercise 3
# 
# def withdraw(balance, amount):
#     logging.debug("withdraw %s", amount)
# 
#     if amount <= 0:
#         logging.error("Error, the amount must be positive")
#         return balance
# 
#     if amount > balance:
#         logging.warning("Warning, not enough mony")
#         return balance
#     
#     new_balance = balance - amount
#     logging.info("The request was successful.")
#     return new_balance
#   
# 
# 
# 
# 
# 
# 
# 
#  
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