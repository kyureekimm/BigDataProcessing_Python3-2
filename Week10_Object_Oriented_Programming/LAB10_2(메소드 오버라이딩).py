class Bank:
    def __init__(self, name):
        self.name = name
        
    def get_interest_rate(self):
        return 0.0

class BadBank(Bank):
    def __init__(self):
        super().__init__("BadBank")

    def get_interest_rate(self):
        return 10.0

class NormalBank(Bank):
    def __init__(self):
        super().__init__("NormalBank")

    def get_interest_rate(self):
        return 5.0

class GoodBank(Bank):
    def __init__(self):
        super().__init__("GoodBank")
        
    def get_interest_rate(self):
        return 3.0

banks = [BadBank(), NormalBank(), GoodBank()]

for bank in banks:
    print(f"{bank.name} 의 이자율: {bank.get_interest_rate()}")