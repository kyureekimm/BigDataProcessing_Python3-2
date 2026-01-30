class SecretAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("입금 금액이 올바르지 않습니다")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("잔액 부족")
        elif amount <= 0:
            print("출금 금액이 올바르지 않습니다")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

initial = int(input("초기 자본을 입력하세요: "))
account = SecretAccount(initial)

deposit_amount = int(input("입금할 금액을 입력하세요: "))
account.deposit(deposit_amount)

withdraw_amount = int(input("출금할 금액을 입력하세요: "))
account.withdraw(withdraw_amount)

print("\n=== 거래 결과 ===")
print(f"최종 잔액: {account.get_balance()} 원")