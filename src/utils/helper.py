class ProblemInfo:
    def __init__(self, number, name, variant, takeaway) -> None:
        self.number = number
        self.name = name
        self.variant = variant
        self.takeaway = takeaway

    def display(self):
        print("\n<===================================>")
        print(f'Problem #{self.number}')
        print(f'Name: {self.name}')
        print(f'Difficulty: {self.variant}')
        print("<===================================>")
        pass

    def end(self):
        print(f'\nTake away: {self.takeaway}')
