from employee.employee import Employee
class AdminStaff(Employee):
    """Administrative staff class."""

    def get_income(self) -> float:
        """Income = base salary."""
        return self.basic_salary
