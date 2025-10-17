from abc import ABC, abstractmethod

class Employee(ABC):
    """
    Represent an employee in the management system.
    Đại diện cho một nhân viên trong hệ thống quản lý.
    """

    def __init__(self, emp_id: str, full_name: str, basic_salary: float, department_id: str = None):
        self._id = emp_id
        self._full_name = full_name
        self._basic_salary = basic_salary
        self._department_id = department_id
        self._role = None  # e.g., "HOD" (Head of Department)

    # --- Encapsulated properties ---
    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, new_id: str):
        self._id = new_id

    @property
    def full_name(self) -> str:
        return self._full_name

    @full_name.setter
    def full_name(self, new_name: str):
        self._full_name = new_name

    @property
    def basic_salary(self) -> float:
        return self._basic_salary

    @basic_salary.setter
    def basic_salary(self, new_salary: float):
        if new_salary < 0:
            raise ValueError("Lương cơ bản phải là số không âm.")
        self._basic_salary = new_salary

    @property
    def department_id(self) -> str:
        return self._department_id

    @department_id.setter
    def department_id(self, value: str):
        self._department_id = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, new_role):
        self._role = new_role

    # --- Abstract method ---
    @abstractmethod
    def get_income(self) -> float:
        """Return total income (to be implemented in subclasses)."""
        pass

    def calc_tax(self) -> float:
        """Calculate income tax based on income brackets."""
        taxable_income = self.get_income()
        if taxable_income is None or taxable_income < 0:
            raise ValueError("Thu nhập phải là một số không âm.")

        if taxable_income < 9_000_000:
            return 0.0
        elif taxable_income <= 15_000_000:
            return taxable_income * 0.10
        else:
            return taxable_income * 0.12

    def __str__(self):
        """Vietnamese UI display string."""
        return (
            f"Mã: {self.id} | Họ tên: {self.full_name} | "
            f"Lương cơ bản: {self.basic_salary:,.0f} | "
            f"Thu nhập: {self.get_income():,.0f} | "
            f"Thuế: {self.calc_tax():,.0f}"
        )
