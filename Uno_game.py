import random

def uno_board():
    board = []

    colors = ["Yellow", "Red", "Blue", "Green"]
    values = [0,1,2,3,4,5,6,7,8,9, "Draw two", "Skip", "Reverse"]
    wilds = ["wild", "wild draw four"]

    for color in colors:
        for value in values:
            card_value = "{} {} ".format(color, value)
            board.append(card_value)
            if value != 0:
                board.append(card_value)

    for wild in wilds:
        for _ in range(4):
            board.append(wild)

    print(board)
    return board

def shuffle_deck(board):
    random.shuffle(board)
    return board

def deal_cards(board):
    player_hand = []
    computer_hand = []

    for i in range(7):
        player_hand.append(board.pop())
        computer_hand.append(board.pop())

    print("Your hand:", player_hand)
    print("Computer's hand:", computer_hand)
    return player_hand, computer_hand

def draw_card(board, hand):
    if board:
        hand.append(board.pop())
    else:
        print("The deck is empty!")
    return hand

def play_card(hand, card):
    if card in hand:
        hand.remove(card)
        print(f"Played card: {card}")
    else:
        print("Card not in hand!")
    return hand

def check_winner(player_hand, computer_hand):
    if not player_hand:
        print("You win!")
        return "Player"
    elif not computer_hand:
        print("Computer wins!")
        return "Computer"
    return None

def game_loop():
    board = shuffle_deck(uno_board())
    player_hand, computer_hand = deal_cards(board)

    while True:
        print("\nYour turn:")
        print("Your hand:", player_hand)
        action = input("Type 'play' to play a card or 'draw' to draw a card: ").strip().lower()

        if action == 'play':
            card = input("Enter the card you want to play: ").strip()
            player_hand = play_card(player_hand, card)
        elif action == 'draw':
            player_hand = draw_card(board, player_hand)
        else:
            print("Invalid action. Please type 'play' or 'draw'.")

        winner = check_winner(player_hand, computer_hand)
        if winner:
            break

        print("\nComputer's turn:")
        if computer_hand:
            computer_card = computer_hand[0]
            computer_hand = play_card(computer_hand, computer_card)
        else:
            computer_hand = draw_card(board, computer_hand)

        winner = check_winner(player_hand, computer_hand)
        if winner:
            break



def main():
    uno_board()
    shuffled_board = shuffle_deck(uno_board())
    deal_cards(shuffled_board)
    draw_card(shuffled_board, [])
    play_card([], "Red 5")
    check_winner([], ["Red 5"])
    game_loop()


if __name__ == "__Main__":
    main()