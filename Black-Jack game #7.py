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
        self.value += values[card.rank] #calculates the card value based on the card rank
        if card.rank == 'Ace': #special requirement for ace
            self.aces += 1     #adjustment for ace
    
    def adjust_for_ace(self): 
        while self.value > 21 and self.aces: #decreases the aces's value from 11 to 1 to stay under 21
            self.value -= 10 
            self.aces -= 1

#creating Chips balance for comeptitor           

class Chips:
    
    def __init__(self):
        self.total = 100  #Starting value for bets. Can be the default value or changed by the user
        self.bet = 0      
        
    def win_bet(self):
        self.total += self.bet #add bet when you win
    
    def lose_bet(self):
        self.total -+ self.bet #subtract bet when you lose

def take_bet(chips): #function for the program to receive bets from the player
    while True:      #prompts the user for an reasonable integer 
        try:
            chips.bet = int(input('How many chips would you like to bet?  ')) #Asks the player what they want their bet to be
        except ValueError:
            print("Sorry, a bet must be an integer!") #Cannot be anything but a number
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet cannot exceed {} '.format(chips.total)) #sets a maximum number for bets. The player's bet cannot exceed the chips they have already
            else:
                break #stops the function

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand): #function for players taking hits or using stand until bust
    global playing           #global means the variable 'playing' can be accessed inside and outside the function 
    
    while True:              #prompt for the player to hit or stand
        x = input("Would you like to Hit or Stand? Enter 'h' or 's'") #asks for the user's input
        
        if x[0].lower() == 'h':
            hit(deck,hand)  #hit() function. Hit for h

        elif x[0].lower() == 's':
            print("You chose to stand. Luigi is playing.") #informs player
            playing = False #stand for s

        else:
            print("Sorry, please try again.") #neither is selected. Prompts player to try again
            continue #continues asking afterwards
        break        #stops function

def show_some(player,dealer): #function to display cards during the game
    print("\nLuigi's Hand")
    print("<card hidden>")
    print(' ', dealer.cards[1])
    print("\nYour Hand: ", *player.cards, sep= '\n')
        
def show_all(player,dealer): #function to display cards at the end of the game
    print("\nLuigi's Hand:", *dealer.cards, sep="\n")
    print("Luigi's Hand =",dealer.value)
    print("\nYour Hand: ", *player.cards, sep= '\n')
    print("Your Hand = ", player.value)

#functions to for game results

def player_busts(player,dealer,chips): #function for losing the game
    print("You bust!")
    chips.lose_bet()

def player_wins(player,dealer,chips): #function for winning the game
    print("You win!")
    chips.win_bet()

def dealer_busts(player,dealer,chips): #function for dealer losing the game
    print("Luigi busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips): #function for dealer winning the game
    print("Luigi wins!")
    chips.lose_bet()
    
def push(player,dealer): #function for a tied game
    print("Both players tie! It is a push.") 