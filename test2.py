def check_number(a):
    if a >= 2:
        if a < 7:
            return "Number is between 2 to 7"
        return "Number is greater than 2 and greater than 7"
    return "Number is out of the range of 2 to 7"

a = int(input("Enter a number: "))
result = check_number(a)
print(result)