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
        print(f"Total Budget: ${self.income}")