import time
from operator import itemgetter

def sort_directory(function):
    def define_directory():
        function()
        for row in sorted(directory, key=itemgetter(1)):
            if row[2] == 'M':
                print(f'Mr. {row[0]}')
            elif row[2] == 'F':
                print(f'Ms. {row[0]}')
    return define_directory

def validate_data(split_list):
    try:
        if len(split_list) < 4:
            return False
        if split_list[-1].upper() not in ['M', 'F']:
            return False
        int(split_list[-2])
        return True
    except ValueError:
        return False

directory = []
@sort_directory
def main():
    print(
        """
        ****************************************************************************************************************************************
            This is the second test.
            First you have to put the size of directory, after that you have to input the information with next format type (separed by spaces):
            first_name, last_name, age, sex(M or F)
        ****************************************************************************************************************************************
        """
    )
    try:

        range_list = int(input("List Size: "))
        if range_list < 1 or range_list > 10:
            print("The list size range is 1 to 10...")
            time.sleep(2)
            main()
        iterator = 0
            
        while iterator < range_list:
            person = input(f"Person #{iterator+1}: ")
            split_list = person.split(" ")
            if validate_data(split_list):
                iterator += 1
                print("Is valid!!!")
                sex = split_list[-1].upper()
                age = split_list[-2]
                names = " ".join(split_list[0:-2])
                directory.append([names, age, sex])
            else:
                print("Please validate format data and insert again...")
    except ValueError as e:
        print("Please choice a valid option...")
        time.sleep(2)
        main()