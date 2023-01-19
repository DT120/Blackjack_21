import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value in range(2, 11) for suit in ["hearts", "diamonds", "clubs", "spades"]]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def score(self):
        return sum(card.value for card in self.hand)

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def play(self):
        self.deck.shuffle()
        self.player.hand.append(self.deck.draw())
        self.player.hand.append(self.deck.draw())
        self.dealer.hand.append(self.deck.draw())
        self.dealer.hand.append(self.deck.draw())

        while True:
            choice = input(f"{self.player.name}, do you want to hit or stay? ").lower()
            if choice == "hit":
                self.player.hand.append(self.deck.draw())
                if self.player.score() > 21:
                    print("You bust!")
                    break
            elif choice == "stay":
                break

        while self.dealer.score() < 17:
            self.dealer.hand.append(self.deck.draw())
            if self.dealer.score() > 21:
                print("Dealer bust!")
                break

        if self.player.score() > self.dealer.score() or self.dealer.score() > 21:
            print("You win!")
        elif self.player.score() < self.dealer.score():
            print("You lose!")
        else:
            print("It's a tie!")

game = Blackjack()
game.play()
