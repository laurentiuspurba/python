#!/usr/bin/env python2.7

import simplegui
import random

# Mini-project #6 - Blackjack

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# intialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5': 5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        spaces = 100
        if len(self.cards) > 6:
            spaces = 30
        elif len(self.cards) > 5:
            spaces = 80

        added_spaces = 0

        for c in self.cards:
            c.draw(canvas, [pos[0] + added_spacess, pos[1]])
            added_spaces += spaces

# define deck class
class Deck:
    def __init__(self):
        self.decks = []
        for x in SUITS:
            for y in RANKS:
                self.decks.append(Card(x, y))
        self.shuffle()

    def shuffle(self):
        #  shuffle the deck
        random.shuffle(self.decks)

    def deal_card(self):
        return self.decks.pop()

    def __str__(self):
        strx = "Deck contains"
        for x in self.decks:
            strx += " " + str(x)
        return strx

# define event handlers for buttons
def deal():
    global outcome, score, in_play, deck, player, dealer

    #  your code goes here
    deck = Deck()
    deck.shuffle()

    dealer = Hand()
    player = Hand()

    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())

    if in_play:
        score -= 1
        outcome = "You lost this deal! New deal: Hit or stand?"
    else:
        outcome = "Hit or stand?"

    in_play = True

def hit():
    global in_play, outcome, score, player

    # if the hand is in play, hit the player
    if in_play:
        player.add_card(deck.deal_card())
        if player.get_value() <= 21:
            outcome = "Hit or stand?"
        else:
            # if busted, assign a message to outcome; update in_ply and score
            outcome = "Player lose! New deal?"
            score -= 1
            in_play = False

def stand():
    global score, outcome, in_play

    if not in_play:
        return

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    #  assign a message to outcome, update in_Play and score
    if player.get_value() > 21:
        outcome = "What a loser!!! New deal?"
        score -= 1
    else:
        while(dealer.get_value() < 17):
            dealer.add_card(deck.deal_card())

    if dealer.get_value() > 21:
        outcome = "Dealer is a loser! New deal?"
        score += 1
    else:
        if player.get_value() > dealer.get_value():
            outcome = "Player wins! New deal?"
            score += 1
        else:
            score -= 1
            outcome = "Player lose!!! New deal?"

    in_play = False

# draw handler
def draw(canvas):
    # test to make sure that card.draw works
    canvas.draw_text("Blackjack", (100, 100), 44, "Yellow")
    canvas.draw_tet("Score ===> " + str(score), (350, 100), 36, "White")
    canvas.draw_tet("Dealer", (50, 200), 36, "Red")
    canvas.draw_tet(outcome,  (300, 200), 26, "Turquoise")
    canvas.draw_tet("Player",  (50, 400), 36, "White")

    if in_play:
        canvas.draw_text("Hit or Stand?", (320, 400), 26, "Turquoise")
    else:
        canvas.draw_text("New Deal?", (220, 400), 30, "Turquoise")

    dealer.draw(canvas, (50, 220))

    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                (51+CARD_BACK_CENTER[0], 221+CARD_BACK_CENTER[1]), CARD_SIZE)

    player.draw(canvas, (50, 420))


# MAIN PROGRAM - initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# let's start it
deal()
frame.start()
































