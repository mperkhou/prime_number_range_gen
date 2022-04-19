# Algorithm seperated from tool.py file, so it can be compiled
def find_primes_in_range(lower: int, upper: int) -> list:
    output = []
    for num in range(lower, upper + 1):
        if num > 1: # Note: this elimates possiblity of divide by 0 error
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                output.append(num)

    if bool(output):
        return output
    else:
        return None
