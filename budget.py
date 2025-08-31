"""
Calculates and displays a budget amount.

Attributes:
    income (list): List of incomes.
    expenses (list): List of expenses.
"""
class Budget:
    """
    Initializes the budget to a value.

    Parameters:
    income (list): The initial budget amount.
    """
    def __init__(self, income):
        self.income = income

    """
    Displays the current budget amount.
    """
    def showAmount(self):
        print(f"Total Budget: ${self.income: .2f}")

    def addIncome(self, name, amount):
        """
        Adds an income amount to the budget.

        Parameters:
        name (str): The name of the income source.
        amount (float): The income amount to be added.
        """
        self.name = name
        self.income += amount
        print(f"Added income: {self.name} of ${amount: .2f}")