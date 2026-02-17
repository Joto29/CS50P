import random

coin = random.choice(["Head", "Tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["Jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
