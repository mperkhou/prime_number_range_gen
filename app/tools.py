from gettext import find
from find_primes import find_primes_in_range
def findPrimes(input1: str, input2: str) -> list:
    #   check to make sure inputs are valid integers
    try:
        input1 = int(input1)
    except ValueError as err:
        print(f"Input error: '{input1}' is not an valid integer")
        return err
    else:
        input1 = int(input1)
    
    try:
        input2 = int(input2)
    except ValueError as err:
        print(f"Input error: '{input2}' is not an valid integer")
        return err
    else:
        input2 = int(input2)

    #   Make sure both integers are positive
    if input1 < 0 or input2 <0:
        print("Error: Input range must consist of non negative integers")
        return ValueError

    #   check & correct for order of user input range
    lower, upper = min(input1, input2), max(input1, input2)

    #   Find and append all prime numbers from range to empty output list
    output = find_primes_in_range(lower, upper)
    if bool(output):
        return output
    else:
        print(f"There are no prime numbers in the range of {lower} - {upper} ")
        return None
