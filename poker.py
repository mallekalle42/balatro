# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:08:49 2024

@author: Malle
"""

from poker_modules import *

'initialize conditions'
#type in starterdeck, abandoneddeck, checkereddeck or erraticdeck here
deck = Erratic_Deck()
#convert_clubs_to_hearts(deck, 9)
#add or subtract cards via add/subtract(deck, amount, rank, suit)
#deck = subtract(deck,0,12,1)
#deck = add(deck, 0, 12, 0)
handsize=8
reps=10000;


results_df=simulate_tests(reps,deck.shape[0],handsize,deck)

    
# Erstellen eines leeren DataFrames für die Ergebnisse
#result_df = pd.DataFrame(columns=['Handgröße', 'Pair', 'Triple', 'Full House', 'Fours', 'Flush', 'Straight', 
#                                       'Two Pair', 'Straight Flush', 'Fiver', 'Flush House', 'Flush Five'])
    



# Ergebnis speichern
results = vary_handsize(deck,reps, 5, 15)



# Daten plotten
plt.figure(figsize=(12, 8))

# Lese den Decktyp aus Zeile 12
deck_type = re.findall(r'deck = (.+?)\(\)', open(__file__).read())[0]



# Marker für jede Linie definieren
markers = ['o', 's', 'D', '^', 'v', '>', '<', '*', 'x', 'P', 'p']

# Schleife über die Spalten der Ergebnistabelle und Plotten der Daten mit unterschiedlichen Markern
for i, column in enumerate(results.columns[1:]):
    plt.plot(results['Hand Size'], results[column], marker=markers[i], label=column)

# Titel und Beschriftungen hinzufügen
plt.title(deck_type+"")
plt.xlabel('Hand Size')
plt.ylabel('Propability for each Hand without discards in %')
plt.legend()

# Gitter hinzufügen
plt.grid(True)

# Plot anzeigen
plt.show()
















