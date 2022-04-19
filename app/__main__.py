from tools import findPrimes

def main():
    #   User input
    lower = input("Enter lower bound: ")
    upper = input("Enter Upper Bound: ")
    
    #   Calculate and output results
    result = findPrimes(lower, upper)
    if result:
        print(f"Prime numbers in range {lower} & {upper} : {result} ")
        return result
    else:
        return None
if __name__ == '__main__':
    main()