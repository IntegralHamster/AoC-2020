from collections import deque


def score(deck):
    i = len(deck)
    tot = 0
    while deck:
        curr = deck.popleft()
        tot += i * curr
        i -= 1
    return tot


def game(deck_1, deck_2):
    while deck_1 and deck_2:
        card1 = deck_1.popleft()
        card2 = deck_2.popleft()
        if card1 > card2:
            deck_1.append(card1)
            deck_1.append(card2)
        else:
            deck_2.append(card2)
            deck_2.append(card1)
    return


def copy_cards(deck, card):
    new_deck = deque()
    for i in range(card):
        new_deck.append(deck.popleft())
    return new_deck


def retarded_game(deck_1, deck_2):
    deck_configuration = [[tuple(deck_1), tuple(deck_2)]]
    fla = 0
    while deck_1 and deck_2:
        if ([tuple(deck_1), tuple(deck_2)] in deck_configuration) and fla:
            return 1
        else:
            # print(tuple(deck_1), tuple(deck_2))
            fla = 1
            deck_configuration.append([tuple(deck_1), tuple(deck_2)])
        card1 = deck_1.popleft()
        card2 = deck_2.popleft()
        if card1 <= len(deck_1) and card2 <= len(deck_2):
            result = retarded_game(copy_cards(deck_1.copy(), card1), copy_cards(deck_2.copy(), card2))
        else:
            result = 1 + (card2 > card1)
        if result == 1:
            deck_1.append(card1)
            deck_1.append(card2)
        else:
            deck_2.append(card2)
            deck_2.append(card1)
    if deck_1:
        return 1
    else:
        return 2


f = open('input', 'r')
deck1 = deque()
deck2 = deque()
flag = 1
for line in f:
    if line == '<>':
        break
    line = line.strip()
    if line == 'Player 2:':
        flag = 2
    if line[0] != 'P':
        if flag == 1:
            deck1.append(int(line))
        else:
            deck2.append(int(line))
# game(deck1, deck2)
end = retarded_game(deck1, deck2)
print(score(deck1), score(deck2))
