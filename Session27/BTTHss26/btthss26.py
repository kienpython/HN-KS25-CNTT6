from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
    def display_info(self):
        print(self.employee_id)
        print(self.name)

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus
    def calculate_salary(self):
        salary = self.base_salary + self.bonus
        return salary
    def display_info(self):
        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: Full-time")

class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate
    def calculate_salary(self):
        return self.working_hours * self.hourly_rate
    def display_info(self):
        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: Part-time")

class InternEmployee(Employee):
    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)
        self.allowance = allowance
    def calculate_salary(self):
        return self.allowance
    def display_info(self):
        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: Intern")


employees = [
    FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
    PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
    InternEmployee("E003", "Le Van C", 3000000)
]
def display_info(employees):
    print("--- Danh sach nhan vien---")
    for employee in employees:
        employee.display_info()

def display_salaries(employees):
    print("--- BẢNG LƯƠNG NHÂN VIÊN ---")
    for employee in employees:
        print(f"{employee.employee_id} | {employee.name} | Lương: {employee.calculate_salary():,.0f} VND")

def main():
    while True:
            print('=== EMPLOYEE SALARY MANAGER ===')
            print('1. Xem danh sách nhân viên')
            print('2. Tính lương toàn bộ nhân viên')
            print('3. Thoát chương trình')
            choice = input("Vui long nhap lua chon tu 1-3: ")
            match choice:
                case "1":
                    display_info(employees)
                case "2":
                    display_salaries(employees)
                case "3":
                    print('Cảm ơn bạn đã sử dụng Employee Salary Manager!')
                    break
                case _:
                    print("lua chon khong hop le!")

if __name__ == "__main__":
    main()
    