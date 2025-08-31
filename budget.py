class Budget:
    def __init__(self, amount):
        self.amount = amount

    def showAmount(self):
        print(f"Total Budget: ${self.amount}")