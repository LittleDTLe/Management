import employee
import login

#PROBLEM:
#NEED TO LOGIN BUT CANNOT LOGIN WITHOUT INITIALIZING login()
#


def main():
    menu()


def menu():
    logged = False
    while True:
        if logged == False:
            try:
                selection = int(input("1. LOGIN\n"
                                      "2. SEARCH\n"))
            except:
                print("INVALID SELECTION!")
                exit()
            if selection == 1:
                manager = login()
                log = manager.log()
                if log:
                    logged = True
            else:
                employee.Employee.specEmployee(employee)

        else:
            try:
                selection = int(input("1. CREATE EMPLOYEE\n"
                                    "2. CREATE MANAGER\n"
                                    "3. DELETE EMPLOYEE\n"
                                    "4. DELETE MANAGER\n"))
            except:
                print("INVALID SELECTION!")
                exit()

if __name__ == "__main__":
    main()