import time
from first import main as first_test
from second import main as second_test
from third import main as third_test
from fourth import main as fourth_test

class TecnicalTest():
    def menu(self):
        print(
            """
            **********************************
            Technical Test MVM
            Wich test do you want to execute?
            Options:
            1. Test #1 (Postal Code)
            2. Test #2 (Name Directory)
            3. Test #3 (Valid Email)
            4. Test #4 (Prime Number)
            **********************************
            """
        )
        try:
            option = int(input("Choice option: "))
            if option == 1:
                first_test()
            elif option == 2:
                second_test()
            elif option == 3:
                third_test()
            elif option == 4:
                fourth_test()
            else:
                print("Please choice a valid option...")
                time.sleep(2)
                self.menu()
        except ValueError as e:
            print("Please choice a valid option...")
            time.sleep(2)
            self.menu()


obj = TecnicalTest()
obj.menu()