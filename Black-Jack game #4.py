import random #picks a random variable for the cards 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

#creating card class. This creates our cards/objects

class Card:

    def __init__(self, suit, rank): #Makes the object. Self refers to the card
        self.suit = suit #Describes object value
        self.rank = rank #Describes object value
    
    def __str__(self):
        return self.rank + ' of ' + self.suit #says what specific card 

#creating deck class, shuffle function, and single dialing

class Deck:

    def __init__(self): #Makes object.  Self refers to deck
        self.deck = []  #starts off empty
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self): #Makes object. 
        deck_comp = '' #deck when the game begins. It is empty
        for card in self.deck:
            deck_comp += '\n' + card.__str__() #adds each card object's strings for total
        return 'The deck has' + deck_comp #says total
            
    def shuffle(self): #Shuffle function. Chooses cards randomly
        random.shuffle(self.deck) #shuffles the cards in the deck
        
    def deal(self): #Function to deal the cards 
        single_card = self.deck.pop() #removes the last card from the deck/list
        return single_card #returns the last card. It is stored here
    
#creating a hand for the player and opponent

class Hand:
    def __init__(self):  #cards the player start with
        self.cards = []  # start with an empty list that holds the cards. This similar to what happened with the the Deck class.
        self.value = 0   # start with zero value. Changes when a card is applied to the hand.
        self.aces = 0    # add an attribute to keep track of aces. Aces are special because they have multiple values.
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace': #special requirement for ace
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

#creating Chips balance for comeptitor           

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -+ self.bet