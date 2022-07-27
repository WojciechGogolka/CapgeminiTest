class Employer():
    def __init__(self, fname: str, lname: str, age: int, job: str, salary: float = 0, bonus: float = 0) -> None:
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.job = job
        self.salary = salary
        self.bonus = bonus
        self.total_salary = self.salary + self.bonus

    def apply_bonus(self, bonus_ammount: float):
        self.bonus = + bonus_ammount
        self.total_salary = self.salary + self.bonus

    def __str__(self) -> str:
        userData = f"Name: {self.first_name} Last name: {self.last_name} Age: {str(self.age)} Job: {self.job} Salary: {str(self.salary)}"
        return userData


class Company():
    def __init__(self, name: str) -> None:
        self.name = name
        self.departments = list()
        self.workers = list()

    def add_worker(self, worker: Employer):
        self.workers.append(worker)

    def show_workers(self):
        for id, worker in enumerate(self.workers):
            print(id, worker)

    def show_departments(self):
        for id, department in enumerate(self.departments):
            print(id, department)

    def remove_worker(self, workerID):
        del self.workers[workerID]


class Department(Company):
    def __init__(self, name: str) -> None:
        self.name = name
        self.users = list()

    def add_department(self, department):
        self.departments.append(department)

    def display_employers(self):
        for id, user in enumerate(self.users):
            print(id, user)

    def add_user(self, user: Employer):
        self.users.append(user)

    def apply_bonus(self, bonus_ammount: float):
        for employer in self.users:
            employer.bonus += bonus_ammount

    def remove_user(self, workerID: int):
        del self.users[workerID]

    def __str__(self) -> str:
        return 'Deparment name: ' + self.name
