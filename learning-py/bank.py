class Bank:
    def __init__(self):
        self.amount = 0

    def give_money(self, how_much):
        self.amount += how_much
    def steal_money(self, how_much_steal):
        if how_much_steal > self.amount:
            print(False)
        else:
            self.amount -= how_much_steal
            print(self.amount)
x = Bank()
print(x.amount)
x.give_money(200)
print(x.amount)
x.steal_money(100)