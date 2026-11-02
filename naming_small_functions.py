# exercise 1

PRICE_FOR_A_DISCOUNT = 500
DISCOUNT = 50

def has_discount(price, quantity):
    total = price * quantity
    if total > PRICE_FOR_A_DISCOUNT:
        total -= DISCOUNT
    return total

print(has_discount(120, 5))
print(has_discount(30, 2))


# exercise 3

PASSED = 55

def calculate_average(list_of_grades:list):
    return sum(list_of_grades) / len(list_of_grades)


def is_passing(list_of_grades:list):
    if calculate_average(list_of_grades) > PASSED:
        return "passed"
    else:
        return "failed"


def print_report(name:str, grades:list):
    print(f"{name}: Averge: {calculate_average(grades)} - {is_passing(grades)}")

print_report("Dana", [80, 85])
print_report("Avi", [50, 46])

# exercise 4

PRICE_ROR_FREE_SHIPPING = 200
POSTAGE = 30

def is_free_shipping(total):
    if total < PRICE_ROR_FREE_SHIPPING:
        return total + POSTAGE

def final_price(total):
    print(f"Final price including shipping: {is_free_shipping(total)}")


# exercise 5
LEN_8 = 8
NUMBERS = ["1","2","3","4","5","6","7","8","9","0"]

def is_valid_password(password):
    for num in NUMBERS:
        if num in password and len(password) >= LEN_8:
            return True
        else:
            return False

print(is_valid_password("abc12345"))
print(is_valid_password("abcdefgh"))
print(is_valid_password("a1"))

