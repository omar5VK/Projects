import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

# ------------------------------CLASSES--------------------

class Card:

    def __init__(self, suit, rank):

      self.suit = suit
      self.rank = rank
      self.value = values[rank.capitalize()]

    def __str__(self):

        return f'{self.rank.capitalize()} of {self.suit}'

class Deck:

    def __init__(self):

        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
              created_card = Card(suit, rank)
              self.deck.append(created_card)

    def __str__(self):
        text = ''
        for card in self.deck:
          text += card.__str__()+'\n'
        return text

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):

        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank.capitalize() == 'Ace':

          self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
          self.value -= 10
          self.aces -= 1

class Chips:

    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):

        self.total += self.bet

    def lose_bet(self):

        self.total -= self.bet


# ------------------------------FUNCTIONS------------------------------

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('Insert the bet $$$ '))
        except:
            print('Insert a valid bet!!!!')
        else:
            if chips.bet > chips.total:
                print(f"You don't have enough chips to bet'")
            else: 
                break

def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing # to control an upcoming while loop
    while True:
        choice = input('\nDo you want hit or stand? [H, S]')
        if choice.capitalize() == 'H':
            hit(deck, hand)
        elif choice.capitalize() == 'S':
            print("\nPlayer stands, is dealer's turn")
            playing = False
        else:
            print('Invalid answer')
            continue
        break

def show_some(player,dealer):
    
    print("\nDealer's Hand: ")
    print("First card hidden")
    print(dealer.cards[1])
    
    print("\nPlayer's Hand: ")    
    for card in player.cards:
        print(card)

def show_all(player,dealer):

    print("\nDealer's Hand: ")    
    for card in dealer.cards:
        print(card)

    print(f"Total value of dealer's hand: {dealer.value}")
    
    print("\nPlayer's Hand: ")    
    for card in player.cards:
        print(card)
        
    print(f"Total value of player's hand: {player.value}")

def player_busts(player, dealer, chips):
    print('PLAYER BUSTS')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('PLAYER WINS')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('DEALER BUSTS!!!')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('DEALER WINS... :c')
    chips.lose_bet()

def push(player, dealer):
    print('Dealer and player tie, its a PUSH!!!')




# ------------------------------NOW ON THE GAME!!!!!!!--------------------
while True:
    # Print an opening statement
    print('WELCOME TO BLACKJACK!!!')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player = Hand()
    player.add_card(deck.deal())    
    player.add_card(deck.deal())
    
    dealer = Hand()
    dealer.add_card(deck.deal())    
    dealer.add_card(deck.deal())    

    # Set up the Player's chips
    chips = Chips()

    # Prompt the Player for their bet
    take_bet(chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value >  21:
            player_busts(player, dealer, chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
        
        while dealer.value < player.value:
            hit(deck, dealer)
            
        # Show all cards
        show_all(player, dealer)
        
        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player, dealer, chips)
        elif dealer.value > player.value:
            dealer_wins(player, dealer, chips)
        elif player.value > dealer.value:
            player_wins(player, dealer, chips)
        else:
            push(player, dealer)
                
    # Inform Player of their chips total
    print(f'\nPlayer chips: {chips.total}')
    # Ask to play again
    new_game = input('\nWould you like to play another hand? Y/N: ')
    
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('\nThank you for playing c:')
    
    break