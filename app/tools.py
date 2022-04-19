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
    output = []
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                output.append(num)
    return output
