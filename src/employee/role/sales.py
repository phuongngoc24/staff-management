from employee.employee import Employee
class SalesStaff(Employee):
    """Sales employee with commission based on sales amount."""

    def __init__(self, emp_id: str, full_name: str, basic_salary: float,
                 department_id: str = None, sales_amount: float = 0.0, commission_rate: float = 0.0):
        super().__init__(emp_id, full_name, basic_salary, department_id)
        self._sales_amount = sales_amount
        self._commission_rate = commission_rate

    @property
    def sales_amount(self) -> float:
        return self._sales_amount

    @sales_amount.setter
    def sales_amount(self, new_sales: float):
        if new_sales < 0:
            raise ValueError("Doanh số phải là số không âm.")
        self._sales_amount = new_sales

    @property
    def commission_rate(self) -> float:
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, new_rate: float):
        if new_rate < 0:
            raise ValueError("Tỉ lệ hoa hồng phải là số không âm.")
        self._commission_rate = new_rate

    def get_income(self) -> float:
        """Income = base salary + (sales_amount × commission_rate)."""
        commission = self.sales_amount * self.commission_rate
        return self.basic_salary + commission
