import random

while True:
    Player = random.randint(2, 26)
    Dealer = random.randint(2, 26)

    while True:
        print(f"Player: {Player}, Dealer: {Dealer}")
        MoreCards = input("Do you want more cards? ")

        if str(MoreCards) == "y":
            Player = Player + random.randint(1, 13)
        else:
            if Player == Dealer:
                print("Dealer Wins") 
            elif Player == 21 or (Player > Dealer and Player < 21):
                print("Player Wins")
            else: 
                print("Dealer Wins")
            break
    PlayAgain = input("Play Again? ")

    if str(PlayAgain) == "n":
        break
    else:
        print('/ffn'*292349)