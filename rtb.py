#!/usr/bin/env python3
import random


def get_suit(card):
    return int((card/13))

def get_color(card):
    return int((card/26))

def get_value(card):
    return int((card%13))

def get_guess(it, seen_cards, curr_flip, deck):
    if it == 0:
        red = 0
        black = 0
        seen_color = 0
        for i in seen_cards:
            if get_color(i) == 1:
                red = red + 1
            else:
                black = black + 1
        if red < black:
            return 1
        if red > black:
            return 0
        else:
            return random.randint(0,1)
    if it == 1:
        seen_value = 0
        high = 0
        low = 0
        for i in seen_cards:
            if get_value(i) > get_value(curr_flip[0]):
                high = high + 1
            if get_value(i) < get_value(curr_flip[0]):
                low = low + 1
        if high > low:
            return "Higher"
        if low > high:
            return "Lower"
        if high == low:
            options = ["Higher","Lower"]
            return random.choice(options)
    
    if it == 2:
        lowc = get_value(curr_flip[0])
        highc = get_value(curr_flip[1])

        cards_seen_outside = 0
        cards_seen_inside = 0

        for i in seen_cards:
            if get_value(i) > highc or get_value(i) < lowc:
                cards_seen_outside = cards_seen_outside + 1
            if get_value(i) < highc and get_value(i) > lowc:
                cards_seen_inside = cards_seen_inside + 1
        
        if cards_seen_outside > cards_seen_inside:
            return("Outside")
        if cards_seen_outside < cards_seen_inside:
            return("Between")
        if cards_seen_outside == cards_seen_inside:
            opt_bo = ["Between","Outside"]
            return random.choice(opt_bo)
    if it == 3:
        h = 0
        d = 0
        c = 0
        s = 0

        for i in seen_cards:
            if get_suit(i) == 0:
                h = h + 1
            if get_suit(i) == 1:
                d = d + 1
            if get_suit(i) == 2:
                c = c + 1
            if get_suit(i) == 3:
                s = s + 1
        x = [h,d,c,s]
        tmp = 100
        suit = 0
        count = 0

        for i in x:
            if i < tmp:
                tmp = i
                suit = count
            count = count + 1
        return suit




