"""
Calculates and displays a budget amount.

Attributes:
    amount (float): The budget amount.
    expenses (list): List of expenses.
"""
class Budget:
    """
    Initializes the budget to a value.

    Parameters:
    amount (float): The initial budget amount.
    """
    def __init__(self, income):
        self.income = income

    """
    Displays the current budget amount.
    """
    def showAmount(self):
        print(f"Total Budget: ${self.income}")