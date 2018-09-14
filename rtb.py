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
        seen_color = 0
        for i in range(len(seen_cards)):
            seen_color = get_color(i) + seen_color
        try:
            avg_color_seen = float(seen_color/len(seen_cards))
        except:
            avg_color_seen = 0.5
        if avg_color_seen < 0.5:
            return 1
        if avg_color_seen > 0.5:
            return 0
        if avg_color_seen == 0.5:
            return random.randint(0,1)
    if it == 1:
        seen_value = 0
        for i in range(len(seen_cards)):
            seen_value = get_value(i) + seen_value
        avg_value_seen = float(seen_value/len(seen_cards))
        if avg_value_seen < get_value(curr_flip[0]):
            return "Higher"
        if avg_value_seen > get_value(curr_flip[0]):
            return "Lower"
        if avg_value_seen == get_value(curr_flip[0]):
            options = ["Higher","Lower"]
            return random.choice(options)
    if it == 2:
        lowc = get_value(curr_flip[0])
        highc = get_value(curr_flip[1])

        cards_seen_outside = 0
        cards_seen_inside = 0

        for i in range(len(seen_cards)):
            if get_value(i) > highc or get_value(i) < lowc:
                cards_seen_outside = cards_seen_outside + 1
            if get_value(i) < highc and get_value(i) > lowc:
                cards_seen_inside = cards_seen_inside + 1
        
        if cards_seen_outside > cards_seen_inside:
            return("Between")
        if cards_seen_outside < cards_seen_inside:
            return("Outside")
        if cards_seen_outside == cards_seen_inside:
            opt_bo = ["Between","Outside"]
            return random.choice(opt_bo)
    if it == 3:
        h = 0
        d = 0
        c = 0
        s = 0

        for i in range(len(seen_cards)):
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




