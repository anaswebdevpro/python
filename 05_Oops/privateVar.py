class Bank:
    def __init__(self):
        self.__balance = 0   # private

    def deposit(self, amount):
        self.__balance += amount

    def show(self):
        print(self.__balance)

my_bank = Bank()
my_bank.deposit(1000)
my_bank.show()
print(my_bank.__balance)  # This will raise an AttributeError because __balance is private  