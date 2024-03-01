# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:26:12 2024

@author: Malle
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:08:49 2024

@author: Malle
"""

import numpy as np 
import matplotlib.pyplot as plt
import random
import pandas as pd
import re


'MAKING AND MODIFYING DECKS'

def Starter_Deck():
    suits = [0,1,2,3]
    ranks = list(range(0,13))
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    return np.array(deck)

def Abandoned_Deck():
    suits = [0,1,2,3]
    ranks = list(range(0,10))
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    return np.array(deck)

def Checkered_Deck():
    suits = [0,1]
    ranks = list(range(0,13))
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
            deck.append((rank, suit))
    return np.array(deck)

def Erratic_Deck():
    deck = []
    for _ in range(52):
        rank = random.randint(0,12)  
        suit = random.choice([0,1,2,3])  # Zufällige Farbe
        deck.append((rank, suit))
    deck.sort()
    return np.array(deck)

def convert_clubs_to_hearts(deck, f):

    hearts_indices = np.where(deck[:, 1] == 0)[0]  # Indizes der Herzkarten im Deck
    clubs_indices = np.where(deck[:, 1] == 3)[0]    # Indizes der Clubskarten im Deck

    # Zufällige Auswahl von f Clubskarten, die in Herzkarten umgewandelt werden sollen
    selected_clubs_indices = random.sample(list(clubs_indices), f)

    # Umwandeln der ausgewählten Clubskarten in Herzkarten
    for index in selected_clubs_indices:
        deck[index, 1] = 0


def convert_values_to_aces(deck, w):
    aces_indices = np.where(deck[:, 0] == 12)[0]  # Indizes der Asskarten im Deck
    selected_values_indices = []

    # Zufällige Auswahl von w verschiedenen Werten, die in Asskarten umgewandelt werden sollen
    while len(selected_values_indices) < w:
        index = random.randint(0, len(deck) - 1)
        if index not in selected_values_indices and index not in aces_indices:
            selected_values_indices.append(index)

    # Umwandeln der ausgewählten Kartenwerte in Asskarten
    for index in selected_values_indices:
        deck[index, 0] = 12


def add(deck, count, rank, suit):
    cards_to_add = np.full((count, 2), (rank, suit), dtype=int)  # Erstelle ein Array mit den neuen Karten
    return np.vstack([deck, cards_to_add])  # Verkette das neue Array mit dem bestehenden Deck
    
    return deck


def subtract(deck, count, rank, suit):
    # Überprüfen, ob genügend Karten im Deck vorhanden sind, um abzuziehen
    if count > len(deck):
        print("Fehler: Nicht genügend Karten im Deck!")
        return None

    # Zählen der Anzahl der übereinstimmenden Karten im Deck
    matching_indices = [index for index, card in enumerate(deck) if (card[0] == rank and card[1] == suit)]
    matching_count = len(matching_indices)

    # Überprüfen, ob genügend übereinstimmende Karten vorhanden sind
    if matching_count < count:
        print(f"Fehler: Nicht genügend Karten mit Rang {rank} und Farbe {suit} im Deck!")
        return None

    # Zufällige Auswahl von Karten zum Entfernen
    indices_to_remove = np.random.choice(matching_indices, count, replace=False)

    # Entfernen der ausgewählten Karten
    new_deck = np.delete(deck, indices_to_remove, axis=0)

    return new_deck











'DRAWING HAND'


def drawhand(deck, handsize):
    # Zufällige Auswahl von Indizes für die Hand
    hand_indices = np.random.choice(len(deck), size=handsize, replace=False)
    
    # Extrahieren der ausgewählten Karten aus dem Deck
    hand = deck[hand_indices]
    
    return hand


'tests'
 
"""def shortcut(ch):
    straight=0
    streak=0
    str=0
    fail=0
    for i in range(13):
        if ch[i,0]>0:
            str=str+1
            fail=0
            if i==12 and str>streak:
                streak=str
        else:
            if fail==0:
                fail==1
            if fail==1:
                fail==0
                    
                if str>streak:
                        streak=str
                str=0
    if streak>4:
        straight=1
    return straight
def fourfingershortcut(ch):
    straight=0
    streak=0
    str=0
    fail=0
    for i in range(13):
        if ch[i,0]>0:
            str=str+1
            fail=0
            if i==12 and str>streak:
                streak=str
        else:
            if fail==0:
                fail==1
            if fail==1:
                fail==0
                    
                if str>streak:
                        streak=str
                str=0
    if streak>3:
        straight=1
    return straight"""


def has_full_house(hand):
    # Initialisiere Zähler für die Anzahl der Vorkommen von Werten
    value_counts = [0] * 13
    
    # Zähle die Anzahl der Vorkommen jedes Werts in der Hand
    for card in hand:
        value_counts[int(card[0])] += 1
    
    # Sortiere die value_counts in absteigender Reihenfolge
    sorted_counts = sorted(value_counts, reverse=True)
    
    # Überprüfe, ob ein Full House vorliegt
    if sorted_counts[0] >= 3 and sorted_counts[1] >= 2:
        return True
    else:
        return False

def has_pair(hand):
    # Initialisiere Zähler für die Anzahl der Vorkommen von Werten
    value_counts = [0] * 13
    
    # Zähle die Anzahl der Vorkommen jedes Werts in der Hand
    for card in hand:
        value_counts[int(card[0])] += 1
    
    # Sortiere die value_counts in absteigender Reihenfolge
    sorted_counts = sorted(value_counts, reverse=True)
    
    # Überprüfe, ob ein Full House vorliegt
    if sorted_counts[0] >= 2:
        return True
    else:
        return False

def has_triple(hand):
    # Initialisiere Zähler für die Anzahl der Vorkommen von Werten
    value_counts = [0] * 13
    
    # Zähle die Anzahl der Vorkommen jedes Werts in der Hand
    for card in hand:
        value_counts[int(card[0])] += 1
    
    # Sortiere die value_counts in absteigender Reihenfolge
    sorted_counts = sorted(value_counts, reverse=True)
    
    # Überprüfe, ob ein Full House vorliegt
    if sorted_counts[0] >= 3:
        return True
    else:
        return False

def has_twopair(hand):
    # Initialisiere Zähler für die Anzahl der Vorkommen von Werten
    value_counts = [0] * 13
    
    # Zähle die Anzahl der Vorkommen jedes Werts in der Hand
    for card in hand:
        value_counts[int(card[0])] += 1
    
    # Sortiere die value_counts in absteigender Reihenfolge
    sorted_counts = sorted(value_counts, reverse=True)
    
    # Überprüfe, ob ein Full House vorliegt
    if sorted_counts[0] >= 2 and sorted_counts[1] >= 2:
        return True
    else:
        return False

def has_fourofakind(hand):
    # Initialisiere Zähler für die Anzahl der Vorkommen von Werten
    value_counts = [0] * 13
    
    # Zähle die Anzahl der Vorkommen jedes Werts in der Hand
    for card in hand:
        value_counts[int(card[0])] += 1
    
    # Sortiere die value_counts in absteigender Reihenfolge
    sorted_counts = sorted(value_counts, reverse=True)
    
    # Überprüfe, ob ein Full House vorliegt
    if sorted_counts[0] >= 4:
        return True
    else:
        return False

def has_fiveofakind(hand):
    # Initialisiere Zähler für die Anzahl der Vorkommen von Werten
    value_counts = [0] * 13
    
    # Zähle die Anzahl der Vorkommen jedes Werts in der Hand
    for card in hand:
        value_counts[int(card[0])] += 1
    
    # Sortiere die value_counts in absteigender Reihenfolge
    sorted_counts = sorted(value_counts, reverse=True)
    
    # Überprüfe, ob ein Full House vorliegt
    if sorted_counts[0] >= 5:
        return True
    else:
        return False

def has_straight(hand):
    sorted_hand = sorted(hand, key=lambda x: x[0])  # Sortiere die Hand nach den Werten
    unique_values = set(card[0] for card in sorted_hand)  # Extrahiere die eindeutigen Kartenwerte

    # Durchlaufe die verschiedenen Möglichkeiten für einen Straight
    for start_value in unique_values:
        end_value = start_value + 4
        if all(value in unique_values for value in range(start_value, end_value + 1)):
            return True  # Es gibt einen Straight in der Hand
    return False  # Es gibt keinen Straight in der Hand

def has_flush(hand):
    # Zähle die Anzahl der Karten jeder Farbe
    suits_count = [0] * 4
    for card in hand:
        suits_count[card[1]] += 1
    
    # Überprüfe, ob eine Farbe fünfmal oder öfter vorkommt
    for count in suits_count:
        if count >= 5:
            return True
    return False

def has_straight_flush(hand):
    # Sortiere die Hand nach Wert und Farbe
    sorted_hand = sorted(hand, key=lambda x: (x[0], x[1]))

    # Durchlaufe die Hand und überprüfe für jede Farbe, ob ein Straight vorliegt
    for suit in range(4):
        # Filtere die Hand nach der aktuellen Farbe
        suit_cards = [card for card in sorted_hand if card[1] == suit]
        
        # Überprüfe auf einen Straight in der gefilterten Hand
        if has_straight(suit_cards):
            return True
    
    return False

def has_flush_five(hand):
    # Sortiere die Hand nach Wert und Farbe
    sorted_hand = sorted(hand, key=lambda x: (x[0], x[1]))

    # Durchlaufe die Hand und überprüfe für jede Farbe, ob ein Straight vorliegt
    for suit in range(4):
        # Filtere die Hand nach der aktuellen Farbe
        suit_cards = [card for card in sorted_hand if card[1] == suit]
        
        # Überprüfe auf einen Straight in der gefilterten Hand
        if has_fiveofakind(suit_cards):
            return True
    
    return False

def has_flush_house(hand):
    # Sortiere die Hand nach Wert und Farbe
    sorted_hand = sorted(hand, key=lambda x: (x[0], x[1]))

    # Durchlaufe die Hand und überprüfe für jede Farbe, ob ein Straight vorliegt
    for suit in range(4):
        # Filtere die Hand nach der aktuellen Farbe
        suit_cards = [card for card in sorted_hand if card[1] == suit]
        
        # Überprüfe auf einen Straight in der gefilterten Hand
        if has_fiveofakind(suit_cards):
            return True
    
    return False







#SIMULATIONS

                 
def simulate_tests(reps, deckgr, handsize, deck):
    results = {'Label': ['Pair', 'Triple', 'Full House', 'Fours', 'Flush', 'Straight', 'Two Pair', 'Straight Flush', 'Fiver','Flush House','Flush Five'],
               'Anzahl': [0] * 11,
               'Chance': [0.0] * 11}

    for j in range(reps):
        hand = drawhand(deck, handsize)
        
        results['Anzahl'][0] += has_pair(hand)
        results['Anzahl'][1] += has_triple(hand)
        results['Anzahl'][2] += has_full_house(hand)
        results['Anzahl'][3] += has_fourofakind(hand)
        results['Anzahl'][4] += has_flush(hand)
        results['Anzahl'][5] += has_straight(hand)
        results['Anzahl'][6] += has_twopair(hand)
        results['Anzahl'][7] += has_straight_flush(hand)
        results['Anzahl'][8] += has_fiveofakind(hand)
        results['Anzahl'][9] += has_flush_house(hand)
        results['Anzahl'][10] += has_flush_five(hand)

    for i in range(len(results['Label'])):
        results['Chance'][i] = results['Anzahl'][i] / reps * 100

    return pd.DataFrame(results)




def vary_handsize(deck,reps, handstart, handend):
    # Anzahl der Wiederholungen der Simulation
    
    # Erstellen eines leeren DataFrames für die Ergebnisse
    result_df = pd.DataFrame(columns=['Hand Size', 'Pair', 'Triple', 'Full House', 'Fours', 'Flush', 'Straight', 
                                       'Two Pair', 'Straight Flush', 'Fiver', 'Flush House', 'Flush Five'])
    
    # Durchlaufen der Handgrößen von 5 bis 15
    for handsize in range(handstart, handend+1):
        # Simulation durchführen und Ergebnisse erhalten
        results = simulate_tests(reps, deck.shape[0], handsize, deck)
        
        # Ergebnisse in die Ergebnistabelle einfügen
        new_row = {'Hand Size': handsize,
                   'Pair': results.loc[0, 'Chance'],
                   'Triple': results.loc[1, 'Chance'],
                   'Full House': results.loc[2, 'Chance'],
                   'Fours': results.loc[3, 'Chance'],
                   'Flush': results.loc[4, 'Chance'],
                   'Straight': results.loc[5, 'Chance'],
                   'Two Pair': results.loc[6, 'Chance'],
                   'Straight Flush': results.loc[7, 'Chance'],
                   'Fiver': results.loc[8, 'Chance'],
                   'Flush House': results.loc[9, 'Chance'],
                   'Flush Five': results.loc[10, 'Chance']}
        
        result_df = pd.concat([result_df, pd.DataFrame([new_row])], ignore_index=True)
    
    return result_df
    













