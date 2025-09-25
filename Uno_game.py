import random

def make_deck():
    colors = ["Red", "Yellow", "Green", "Blue"]
    values = list(range(0,10)) + ["Skip", "Reverse", "Draw Two"]
    deck = []

    for c in colors:
        for v in values:
            card = f"{c} {v}"
            deck.append(card)
            if v != 0:
                deck.append(card)

    for i in range(4):
        deck.append("Wild")
        deck.append("Wild Draw Four")
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def deal(deck):
    player = []
    computer = []
    for i in range(7):
        player.append(deck.pop())
        computer.append(deck.pop())
    return player, computer

def can_play(card, top_card, current_color):
    if "Wild" in card:
        return True
    try:
        color1, value1 = top_card.split(" ", 1)
        color2, value2 = card.split(" ", 1)
    except ValueError:
        return False
    return color2 == current_color or value1 == value2

def choose_color():
    while True:
        color = input("Choose a color (Red, Yellow, Green, Blue): ").capitalize()
        if color in ["Red", "Yellow", "Green", "Blue"]:
            return color
        else:
            print("Invalid color, try again.")

def main():
    print("🎉 Welcome to UNO! 🎉")
    print("Instructions:")
    print("1. You start with 7 cards.")
    print("2. On your turn type 'play' or 'draw'.")
    print("3. You can only play a card if it matches the color or number.")
    print("4. Special cards: Skip, Reverse, Draw Two, Wild, Wild Draw Four.")
    input("Press ENTER to start the game...")

    deck = make_deck()
    shuffle_deck(deck)
    player, computer = deal(deck)

    discard = [deck.pop()]
    if "Wild" in discard[-1]:
        current_color = choose_color()
    else:
        current_color = discard[-1].split(" ",1)[0]

    skip_turn = False
    while True:
        print("\nTop of discard pile:", discard[-1])
        print("Your hand:", player)

        # PLAYER TURN
        if not skip_turn:
            move = input("Do you want to 'play' or 'draw'? ").lower()

            if move == "play":
                card = input("Which card? Type exactly (e.g. 'Red 5'): ")
                if card in player and can_play(card, discard[-1], current_color):
                    player.remove(card)
                    discard.append(card)
                    print("You played:", card)

                    if "Wild Draw Four" in card:
                        current_color = choose_color()
                        for _ in range(4):
                            if deck: computer.append(deck.pop())
                        skip_turn = True
                    elif "Wild" in card:
                        current_color = choose_color()
                    elif "Draw Two" in card:
                        for _ in range(2):
                            if deck: computer.append(deck.pop())
                        skip_turn = True
                        current_color = card.split(" ",1)[0]
                    elif "Skip" in card or "Reverse" in card:
                        skip_turn = True
                        current_color = card.split(" ",1)[0]
                    else:
                        current_color = card.split(" ",1)[0]
                else:
                    print("❌ You can't play that card!")
            elif move == "draw":
                if deck:
                    new_card = deck.pop()
                    player.append(new_card)
                    print("You drew:", new_card)
                else:
                    print("Deck is empty!")
            else:
                print("Invalid choice!")
        else:
            print("Your turn is skipped!")
            skip_turn = False

        if len(player) == 0:
            print("🎉 You win!")
            break

        # COMPUTER TURN
        if not skip_turn:
            print("\n--- Computer's turn ---")
            played = False
            for c in computer:
                if can_play(c, discard[-1], current_color):
                    computer.remove(c)
                    discard.append(c)
                    print("Computer played:", c)

                    if "Wild Draw Four" in c:
                        current_color = random.choice(["Red","Yellow","Green","Blue"])
                        for _ in range(4):
                            if deck: player.append(deck.pop())
                        skip_turn = True
                    elif "Wild" in c:
                        current_color = random.choice(["Red","Yellow","Green","Blue"])
                        print("Computer chose a color.")
                    elif "Draw Two" in c:
                        for _ in range(2):
                            if deck: player.append(deck.pop())
                        skip_turn = True
                        current_color = c.split(" ",1)[0]
                    elif "Skip" in c or "Reverse" in c:
                        skip_turn = True
                        current_color = c.split(" ",1)[0]
                    else:
                        current_color = c.split(" ",1)[0]

                    played = True
                    break
            if not played:
                if deck:
                    new_card = deck.pop()
                    computer.append(new_card)
                    print("Computer drew a card.")
                else:
                    print("Deck is empty, computer skips.")
        else:
            print("Computer's turn is skipped!")
            skip_turn = False

        if len(computer) == 0:
            print("💻 Computer wins!")
            break

if __name__ == "__main__":
    main()
