from employee.employee import Employee
class Manager(Employee):
    """Manager with responsibility salary."""

    def __init__(self, emp_id: str, full_name: str, basic_salary: float,
                 department_id: str = None, responsibility_salary: float = 0.0):
        super().__init__(emp_id, full_name, basic_salary, department_id)
        self._responsibility_salary = responsibility_salary
        self.role = "HOD"  # Head of Department

    @property
    def responsibility_salary(self) -> float:
        return self._responsibility_salary

    @responsibility_salary.setter
    def responsibility_salary(self, value: float):
        if value < 0:
            raise ValueError("Lương trách nhiệm phải là số không âm.")
        self._responsibility_salary = value

    def get_income(self) -> float:
        """Income = base salary + responsibility salary."""
        return self.basic_salary + self.responsibility_salary
