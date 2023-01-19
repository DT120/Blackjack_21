import random
import sys

# ♥♠️♦️♣️
number_values = [("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10), ("Jack", 10), ("Queen", 10), ("King", 10), ("Ace", 1)]

class Card():
    def __init__(self, suit, number, value):
        self.suit = suit
        self.number = number
        self.value = value
    def __repr__(self):
        return "{number} of {suit}s".format(number = self.number, suit = self.suit)


class Deck():
    def __init__(self):
      # Create a list of card objects for each suit and number value combination
      self.cards = [Card(suit, number, value) for suit in ["♥", "♠️", "♦️", "♣️"] for number, value in number_values]
    def shuffle(self):
       # Shuffle the cards in the deck
        random.shuffle(self.cards)
    def draw(self):
      # Draw a card from the deck
        return self.cards.pop()

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def score(self):
      # Calculate the total value of cards in the player's hand
      score = 0 + sum(card.value for card in self.hand)
      return score

class Blackjack():
    def __init__(self):
        self.deck = Deck()
        self.player = Player(input("Please Input A Name..."))
        self.dealer = Player("Dealer")

    def play(self):
        self.deck.shuffle()
        self.player.hand.append(self.deck.draw())
        self.player.hand.append(self.deck.draw())
        print("You have {value} | {hand}".format(hand = self.player.hand, value = sum(card.value for card in self.player.hand)))

        self.dealer.hand.append(self.deck.draw())
        self.dealer.hand.append(self.deck.draw())
        print("Dealer showing {hand}".format(hand = self.dealer.hand[0]))

        while True:

            ace_card = next((card for card in self.player.hand if card.number == "Ace"), None)
            if self.player.score() <=  11 and ace_card:
              choice = input("You drew an Ace! Would you like to count it as 1 or 11.")
              if choice == "11":
                # Update the value of ace card to 11
                ace_card.value = 11
                print("You have {value} | {hand}".format(hand = self.player.hand, value = sum(card.value for card in self.player.hand)))
              if choice not in ["1", "11"]:
                print("Invalid Input, please enter again")
                choice = input("You drew an Ace! Would you like to count it as 1 or 11...")

              elif choice == "1":
                pass
            if self.player.score() == 21:
                break

            choice = input(f"{self.player.name}, do you want to hit or stay? ")
              
            if choice == "hit":
                self.player.hand.append(self.deck.draw())
                
            print("You have {value} | {hand}".format(hand = self.player.hand, value = sum(card.value for card in self.player.hand)))
                
            if self.player.score() > 21:
                    print("You bust!")
                    print("Dealer Wins!")
                    return
            elif choice == "stay":
                break
          
        ace_card = next((card for card in self.dealer.hand if card.number == "Ace"), None)

        if self.dealer.score() <= 11 and ace_card:
          # Update the value of ace card to 11
            ace_card.value = 11
        
        while self.dealer.score() < 17:
            self.dealer.hand.append(self.deck.draw())
            if self.dealer.score() > 21:
                print("Dealer had {value} | {hand}".format(value = sum(card.value for card in self.dealer.hand), hand = self.dealer.hand))
                print("Dealer bust!")
                print("You win!")
                return

        if (self.player.score() > self.dealer.score() and self.player.score() <= 21) or self.dealer.score() > 21:
            print("Dealer had {value} | {hand}".format(value = sum(card.value for card in self.dealer.hand), hand = self.dealer.hand))
            print("You win!")
        elif self.player.score() < self.dealer.score():
            print("Dealer had {value} | {hand}".format(value = sum(card.value for card in self.dealer.hand), hand = self.dealer.hand))
            print("You lose!")
        else:
            print("Dealer had {value} | {hand}".format(value = sum(card.value for card in self.dealer.hand), hand = self.dealer.hand))
            print("It's a tie!")

def play_game():
    game = Blackjack()
    game.play()
    again = input("Do you want to play again? (yes/no)")
    if again == "yes":
        return
    if again == "no":
      sys.exit()
    if again not in ["yes", "no"]:
      print("Invalid Input, please enter again")
      again = input("Do you want to play again? (yes/no)")
    

while True:
    play_game()

