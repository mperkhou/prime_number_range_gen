from timeit import default_timer
from tools import findPrimes

def main():
    #   User input
    lower = input("Enter lower bound: ")
    upper = input("Enter Upper Bound: ")
    
    #   Calculate and output results, calculate time to complete
    start = default_timer()
    result = findPrimes(lower, upper)
    end = default_timer()
    if result:
        print(f"Prime numbers in range {lower} & {upper} : {result} ")
        print(f"Time elapsed: {end - start} seconds.")
        return result
    else:
        return None
if __name__ == '__main__':
    main()