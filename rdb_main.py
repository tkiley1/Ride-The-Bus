#!/usr/bin/env python
import random

def initialize_deck():
    deck = []
    for i in range(52):
        deck = deck + [i]
    return deck

def flip(deck):
    r = random.randint(0, len(deck))
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
    while((len(deck)/4) > 0):
        guess = get_guess(it, seen_cards, curr_flip, deck)
        card, deck = flip(deck)
        if guess != get_color(card):
            curr_flip = []
            it = 0
            continue
        seen_cards = seen_cards + [card]
        curr_flip = curr_flip + [card]
        it = it + 1
        guess = get_guess(it, seen_cards, curr_flip, deck)
        card, deck = flip(deck)
        if guess == "Higher" and get_value(card) <= curr_flip[0] or (guess == "Lower" and get_value(card) >= curr_flip[0]):
            curr_flip = []
            it = 0
            continue
        seen_cards = seen_cards + [card]
        curr_flip = curr_flip + [card]
        tmp = []
        for i in curr_flip:
            tmp = tmp + get_value(i)
        tmp = sorted(tmp)
        it = it + 1
        guess = get_guess(it, seen_cards, curr_flip, deck)
        card, deck = flip(deck)
        if (guess == "Between" and (get_value(card) >= tmp[0] or get_value(card) <= tmp[1])) or  (guess == "Outside" and (get_value(card) <= tmp[0] or get_value(card) >= tmp[1])):
            curr_flip = []
            it = 0
            continue
        seen_cards = seen_cards + [card]
        curr_flip = curr_flip + [card]
        it = it + 1
        guess = get_guess(it, seen_cards, curr_flip, deck)
        card, deck = flip(deck)
        if guess != get_suit(card):
            curr_flip = []
            it = 0
            continue
        else:
            wins = wins + 1
            games = games + 1
            curr_flip = []
            it = 0
            continue
    return wins, games, float(wins/games)

print(rtb())