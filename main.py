from budget import Budget

class Main:
    totalBudget = Budget(0)
    totalBudget.showAmount()

    totalBudget.addIncome("Software engineering job", 8000)
    totalBudget.showAmount()