from __future__ import annotations
from typing import Optional, List, Dict
from dataclasses import dataclass

# ===== Constants =====
TOP_N_HIGHEST = 5

# ===== Domain models =====
try:
    from your_module import Employee  
except Exception:
    @dataclass
    class Employee:
        id: str
        full_name: str
        basic_salary: float
        department_id: Optional[str] = None
        role: Optional[str] = None

        def total_income(self) -> float:
            return float(self.basic_salary)

# ===== Exceptions =====
class EmployeeNotFoundError(Exception):
    pass

class EmployeeValidationError(Exception):
    pass


# ===== Service =====
class EmployeeService:
    """
    This service is responsible for the business logic of the application.
    """

    def __init__(self):
        self._employees: Dict[str, Employee] = {}  # biến nội bộ dùng snake_case

    # ---------- Helpers ----------
    @staticmethod
    def _income(emp: Employee) -> float:
        if hasattr(emp, "total_income") and callable(emp.total_income):
            return float(emp.total_income())
        return float(getattr(emp, "basic_salary", 0.0))

    def _validate_new(self, employee_data: dict) -> None:
        required_fields = ["id", "full_name", "basic_salary"]
        missing_fields = [k for k in required_fields if k not in employee_data or employee_data[k] in (None, "")]
        if missing_fields:
            raise EmployeeValidationError(f"Missing fields: {', '.join(missing_fields)}")

        try:
            employee_data["basic_salary"] = float(employee_data["basic_salary"])
        except (TypeError, ValueError):
            raise EmployeeValidationError("basic_salary must be a number.")

        if employee_data["basic_salary"] < 0:
            raise EmployeeValidationError("basic_salary cannot be negative.")

        if employee_data["id"] in self._employees:
            raise EmployeeValidationError(f"Employee ID '{employee_data['id']}' already exists.")

    # ---------- 1) CRUD ----------
    def add_employee(self, employee_data: dict) -> Employee:
        """Add a new employee (requires: id, full_name, basic_salary)."""
        self._validate_new(employee_data)
        employee = Employee(
            id=str(employee_data["id"]),
            full_name=str(employee_data["full_name"]),
            basic_salary=float(employee_data["basic_salary"]),
            department_id=employee_data.get("department_id"),
            role=employee_data.get("role"),
        )
        self._employees[employee.id] = employee
        return employee

    def get_all_employees(self) -> List[Employee]:
        """Return all employees (UI can show 'empty list' message if needed)."""
        return list(self._employees.values())

    def find_employee_by_id(self, employee_id: str) -> Employee | None:
        """Find an employee by ID."""
        return self._employees.get(employee_id)

    def delete_employee_by_id(self, employee_id: str):
        """Delete an employee by ID; raise if not found."""
        if employee_id not in self._employees:
            raise EmployeeNotFoundError(f"Employee ID '{employee_id}' not found.")
        del self._employees[employee_id]

    def update_employee(self, employee_id: str, new_data: dict) -> Employee:
        """Update employee by ID; raise if not found."""
        employee = self._employees.get(employee_id)
        if not employee:
            raise EmployeeNotFoundError(f"Employee ID '{employee_id}' not found.")

        if "basic_salary" in new_data:
            try:
                new_basic_salary = float(new_data["basic_salary"])
            except (TypeError, ValueError):
                raise EmployeeValidationError("basic_salary must be a number.")
            if new_basic_salary < 0:
                raise EmployeeValidationError("basic_salary cannot be negative.")
            employee.basic_salary = new_basic_salary

        if "full_name" in new_data and new_data["full_name"]:
            employee.full_name = str(new_data["full_name"])
        if "department_id" in new_data:
            employee.department_id = new_data["department_id"]
        if "role" in new_data:
            employee.role = new_data["role"]

        return employee

    # ---------- 2) Search & Sort ----------
    def find_employees_by_salary_range(self, min_salary: float, max_salary: float) -> List[Employee]:
        """Filter employees by basic_salary in [min_salary, max_salary]."""
        try:
            salary_min, salary_max = float(min_salary), float(max_salary)
        except (TypeError, ValueError):
            raise EmployeeValidationError("Salary bounds must be numbers.")
        if salary_min > salary_max:
            salary_min, salary_max = salary_max, salary_min

        return [
            employee for employee in self._employees.values()
            if salary_min <= float(employee.basic_salary) <= salary_max
        ]

    def sort_employees_by_name(self) -> List[Employee]:
        """Sort employees by full_name (A–Z)."""
        return sorted(self._employees.values(), key=lambda e: e.full_name.casefold())

    def sort_employees_by_income(self) -> List[Employee]:
        """Sort employees by income (ascending)."""
        return sorted(self._employees.values(), key=self._income)

    def get_top_5_employees_by_income(self) -> List[Employee]:
        """Return top-N (default 5) employees by highest income."""
        return sorted(self._employees.values(), key=self._income, reverse=True)[:TOP_N_HIGHEST]
