import math
import time
def is_prime_fast(number):
    if number <= 1 or ( number > 2 and number %2 ==0 ):
        return False
    else:
        for factor in range(2, int(math.sqrt(number))+1):
            if number % factor == 0:
                return False
        return True

def validate_range(range_num):
    primes = []
    for n in range(1, range_num+1):
        if is_prime_fast(n):
            primes.append(n)
    return primes

def main():
    print(
        """
        ****************************
            This is the fourth test.
            Prime numbers in range
        ****************************
        """
    )
    try:
        range_num = int(input("Enter range number, 1 to "))
        print(f"Prime numbers in range 1 to {range_num} :", validate_range(range_num))
    except ValueError as e:
        print("Please insert a valid number...")
        time.sleep(2)
        main()