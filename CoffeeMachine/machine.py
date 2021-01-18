# trying

class Machine:
    res = [400, 540, 120, 9, 550]  # resource quantity
    ing_list = ('water', 'milk', 'beans', 'cups', 'money')  # ingredients names
    state = 'wait_'  # state of machine
    fill_state = 0  # special state for filling

    def __init__(self):
        self.dict_action = {'wait_buy': self.prn, 'buy1': self.buy, 'buy2': self.buy, 'buy3': self.buy,
                            'buyback': self.begin, 'wait_take': self.take, 'wait_remaining': self.remaining,
                            'wait_fill': self.prn}

    def start(self):
        print("Write action (buy, fill, take, remaining, exit):")
        while True:
            keyb = (input())
            if keyb == 'exit':
                break
            else:
                self.action(keyb)

    def begin(self):
        self.state = 'wait_'
        print("\nWrite action (buy, fill, take, remaining, exit):")

    def action(self, inp):
        if self.state == 'fill':
            self.fill(int(inp))
        else:
            command = self.state + inp
            self.state = inp
            self.dict_action[command]()

    def buy(self):
        coffee_list = [(250, 0, 16, 1, -4), (350, 75, 20, 1, -7), (200, 100, 12, 1, -6)]
        receipt = coffee_list[int(self.state) - 1]
        for i in range(5):
            if self.res[i] - receipt[i] < 0:
                print(f'Sorry, not enough {self.ing_list[i]}!')
                break
            else:
                self.res[i] -= receipt[i]
        else:
            print('I have enough resources, making you a coffee!')
        self.begin()

    def fill(self, q):
        self.res[self.fill_state] += q
        self.fill_state += 1
        if self.fill_state < 4:
            self.prn()
        else:
            self.fill_state = 0
            self.begin()

    def take(self):
        print(f"I gave you ${self.res[4]}")
        self.res[4] = 0
        self.begin()

    def remaining(self):
        print(f"""The coffee machine has:
{self.res[0]} of water
{self.res[1]} of milk
{self.res[2]} of coffee beans
{self.res[3]} of disposable cups
{self.res[4]} of money""")
        self.begin()

    def prn(self):
        if self.state == 'buy':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        else:
            prn_tuple = ('Write how many ml of water do you want to add:',
                         'Write how many ml of milk do you want to add:',
                         'Write how many grams of coffee beans do you want to add:',
                         'Write how many disposable cups of coffee do you want to add:')
            print(prn_tuple[self.fill_state])


m = Machine()
m.start()
