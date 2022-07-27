from options import actions
from classes import Company

company = Company('Fields')

while True:
    try:
        option = int(input("""Choose option to perform:
                    1 - Add new employer
                    2 - Apply bonus to employer
                    3 - Remove employer8
                    4 - Add worker to department
                    5 - Remove worker from department
                    6 - Add department
                    7 - Remove department
                    8 - Apply bonus to all employers from department
                    9 - Show workers in selected department
                    10 - Exit
                    """))
        if option in range(1, 10):
            actions(company, option)
        elif option == 10:
            break
        else:
            print("Wrong value found, insert value from given range (1-10)")
    except:
        print("Wrong input found, insert new value")
