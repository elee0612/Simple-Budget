class Budget:
    """
    Calculates and displays a budget amount.

    Attributes:
    income (list): List of incomes.
    expenses (list): List of expenses.
    """
    
    def __init__(self, income):
        """
        Initializes the budget to a value.

        Parameters:
        income (list): The initial budget amount.
        """
        self.income = income

    def showAmount(self):
        """
        Displays the current budget amount.
        """
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