from classes import Employer, Department


def actions(company, action_number):

    if action_number == 1:
        #User1 = Employer('W', 'G', 23, 'Programmer', 3000)
        first_name = input("Insert employer name: ")
        last_name = input("Insert employer last name: ")
        age = int(input("Insert employer age: "))
        job = input("Insert employer job: ")
        salary = float(input("Insert employer salary: "))
        company.add_worker(Employer(first_name, last_name, age, job, salary))
        # company.add_worker(User1)

    if action_number == 2:
        company.show_workers()
        workerID = int(input("Select worker who will get bonus: "))
        bonusAmount = float(input("Insert bonus ammount: "))
        company.workers[workerID].apply_bonus(bonusAmount)

    if action_number == 3:
        company.show_workers()
        workerID = int(input("Select worker to remove: "))
        company.remove_worker(workerID)

    if action_number == 4:
        company.show_workers()
        workerID = int(input("Select worker: "))
        company.show_departments()
        departmentID = int(input("Select department to assign: "))
        company.departments[departmentID].add_user(company.workers[workerID])

    if action_number == 5:
        company.show_departments()
        departmentID = int(input("Select department: "))
        company.departments[departmentID].display_employers()
        workerID = int(input("Select employer to remove from department: "))
        company.departments[departmentID].remove_user(workerID)

    if action_number == 6:
        departmentName = input("Enter new department name: ")
        company.departments.append(Department(departmentName))

    if action_number == 7:
        for id, departments in enumerate(company.departments):
            print(id, departments)
        departmentID = int(input("Select department you want to remove: "))
        del company.departments[departmentID]

    if action_number == 8:
        company.show_departments()
        departmentID = int(input("Select department: "))
        bonus = int(input("Enter the amount of bonus for employers"))
        for user in company.departments[departmentID].users:
            user.apply_bonus(bonus)

    if action_number == 9:
        company.show_departments()
        departmentID = int(input("Select department: "))
        print("Workers in selected department:")
        company.departments[departmentID].display_employers()
