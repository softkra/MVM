import time
import re
regex_integer_in_range = r"^[1-9]\d{4,7}$"
regex_integer_in_repetitive_pair = r"(\d)(?=\d\1)"
def main():
    print(
        """
        ****************************
            This is the first test.
            Postal Code
        ****************************
        """
    )
    try:
        code = input("Postal Code: ")
        int(code) #Validate number 
        validation = bool(re.match(regex_integer_in_range, code)) and len(re.findall(regex_integer_in_repetitive_pair, code)) < 2
        print("Is a valid postal code? ---> ", validation)
        time.sleep(2)
        main()
    except ValueError as e:
        print("Please insert a valid number...")
        time.sleep(2)
        main()