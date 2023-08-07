#python_lst272.py

class Card:
    suits = ['pik', 'kier',
             'karo', 'trefl']
    values = [None, None, '2', '3', '4',
              '5', '6', '7', '8', '9', '10',
              'waleta', 'damę', 'króla', 'asa']

    def __init__(self, value, suit):
        '''listy suit i value to liczby całkowite'''
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        return self.values[self.value]\
               + ' '\
               + self.suits[self.suit]

#python_lst276.py

from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

#python_lst278.py

class Player:
    def __init__(self, name):
        self.winss = 0
        self.card = None
        self.name = name

#python_lst279.py

class Game:
    def __init__(self):
        name1 = input('Imię gracza 1: ')
        name2 = input('Imię gracza 2: ')
        self.deck = Deck()
        self.pay1 = Player(name1)
        self.pay2 = Player(name2)

    def winsa(self, WINERR):
        w = 'Tę rundę wygrywa {}\n'
        w = w.format(WINERR)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = '{} wyciągnął {}, {} wyciągnął {}\n'
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print('Zaczynamy rozgrywkę!')
        while len(cards) >= 2:
            m = 'Naciśnij q aby zakończyć ' + \
                'lub inny klawisz, aby kontynuować grę: \n'
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.pay1.name
            p2n = self.pay2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.pay1.winss += 1
                self.winsa(self.pay1.name)
            else:
                self.pay2.winss += 1
                self.winsa(self.pay2.name)
                
        win = self.winner(self.pay1,
                          self.pay2)
        print('Wojna skończona - wygrał {}'.format(win))

    def winner(self, p1, p2):
        if p1.winss > p2.winss:
            return p1.name
        if p1.winss < p2.winss:
            return p2.name
        return 'Jest remis!'

game = Game()
game.play_game()
