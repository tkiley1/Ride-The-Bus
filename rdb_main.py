#!/usr/bin/env python
import random
from rtb import *

def initialize_deck():
    deck = []
    for i in range(52):
        deck = deck + [i]
    return deck

def flip(deck):
    r = random.randint(0, len(deck)-1)
    tmp = deck[r]
    deck.remove(tmp)
    return tmp, deck

def rtb():
    deck = initialize_deck()
    seen_cards = []
    curr_flip = []
    it = 0
    wins = 0
    games = 0
    while(len(deck) >= 4):
        guess = get_guess(it, seen_cards, curr_flip, deck)
        #print (guess)
        card, deck = flip(deck)
        #print(seen_cards)
        #print(deck)
        seen_cards = seen_cards + [card]
        if guess != get_color(card):
            curr_flip = []
            it = 0
            games = games + 1
         #   print("Fucked up the color")
            continue
        curr_flip = curr_flip + [card]
        #print(seen_cards)
        #print(deck)
        it = it + 1
        guess = get_guess(it, seen_cards, curr_flip, deck)
        #print(guess)
        card, deck = flip(deck)
        seen_cards = seen_cards + [card]
        if (guess == "Higher" and get_value(card) <= get_value(curr_flip[0])) or (guess == "Lower" and get_value(card) >= get_value(curr_flip[0])):
            curr_flip = []
            it = 0
            games = games + 1
         #   print("Fucked up higher or lower")
            continue
        curr_flip = curr_flip + [card]
        #print(seen_cards)
        #print(deck)
        tmp = []
        for i in curr_flip:
            tmp = tmp + [get_value(i)]
        tmp = sorted(tmp)
        it = it + 1
        guess = get_guess(it, seen_cards, curr_flip, deck)
        #print(guess)
        card, deck = flip(deck)
        seen_cards = seen_cards + [card]
        if ((guess == "Between" and (get_value(card) > tmp[0] and get_value(card) < tmp[1])) or  (guess == "Outside" and (get_value(card) < tmp[0] or get_value(card) > tmp[1]))):
            pass
        else:
            curr_flip = []
            it = 0
            games = games + 1
            #print("Fucked up between or outside")
            continue
        curr_flip = curr_flip + [card]
        #print(seen_cards)
        #print(deck)
        it = it + 1
        guess = get_guess(it, seen_cards, curr_flip, deck)
        #print (guess)
        card, deck = flip(deck)
        seen_cards = seen_cards + [card]
        if guess != get_suit(card):
            curr_flip = []
            it = 0
            games = games + 1
            #print("Fucked up the suit")
            continue
        else:
            wins = wins + 1
            games = games + 1
            curr_flip = []
            it = 0
            #print("Didn't fuck up")
            continue
    return wins, games, 100*(float(wins)/games)
ovr_pct = 0
for i in range(1000000):
    wins, games, pct = rtb()
    ovr_pct = pct + ovr_pct
    print i
ovr_pct = ovr_pct / 1000000
print ovr_pct