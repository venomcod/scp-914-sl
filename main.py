from random import randint


modes = ["rough", "coarse", "1:1", "fine", "very fine"]
cards = ["janitor", "scientist", "research supervisor", "guard", "operative", "captain", "zone manager", "facility", "CI", "O5"]
def upgrade_card(card):
    print(f"Выбери режим прокачки: \n1.Rough \n2.Coarse \n3.1:1 \n4.Fine \n5.Very Fine")
    change = int(input(".>"))
    print(upgrade_O5_card(modes[change - 1]))


def upgrade_janitor_card(mode):
    if mode == "rough" or mode == "coarse":
        return "Destroy"
    elif mode == "1:1":
        return cards[6]
    elif mode == "fine":
        return cards[1]
    elif mode == "very fine":
        r = randint(1, 2)
        if r == 1:
            return cards[1]
        else:
            return cards[2]

def upgrade_scientist_card(mode):
    if mode == "rough":
        r = randint(1,2)
        if r == 1:
            return "Destroy"
        else:
            return cards[0]
    elif mode == "coarse":
        return cards[0]
    elif mode == "1:1":
        return cards[6]
    elif mode == "fine":
        return cards[2]
    elif mode == "very fine":
        r = randint(1, 3)
        if r == 1:
            return cards[1]
        elif r == 2:
            return cards[2]
        else:
            return cards[7]

def upgrade_re_supervisior_card(mode):
    if mode == "rough":
        r = randint(1,2)
        if r == 1:
            return cards[0]
        else:
            return cards[1]
    elif mode == "coarse":
        return cards[1]
    elif mode == "1:1":
        return cards[3]
    elif mode == "fine":
        return cards[7]
    elif mode == "very fine":
        r = randint(1, 2)
        if r == 1:
            return cards[2]
        elif r == 2:
            return cards[7]

def upgrade_guard_card(mode):
    if mode == "rough":
        r = randint(1,2)
        if r == 1:
            return cards[0]
        else:
            return cards[1]
    elif mode == "coarse":
        return cards[1]
    elif mode == "1:1":
        return cards[2]
    elif mode == "fine":
        return cards[4]
    elif mode == "very fine":
        r = randint(1, 3)
        if r == 1:
            return cards[3]
        elif r == 2:
            return cards[4]
        else:
            return cards[5]

def upgrade_operative_card(mode):
    if mode == "rough":
        r = randint(1,2)
        if r == 1:
            return "Destroyed"
        else:
            return cards[3]
    elif mode == "coarse":
        return cards[3]
    elif mode == "1:1":
        return cards[7]
    elif mode == "fine":
        return cards[5]
    elif mode == "very fine":
        r = randint(1, 3)
        if r == 1:
            return cards[4]
        elif r == 2:
            return cards[5]
        else:
            return cards[9]

def upgrade_captain_card(mode):
    if mode == "rough":
        return cards[4]
    elif mode == "coarse":
        return cards[4]
    elif mode == "1:1":
        return cards[8]
    elif mode == "fine":
        return cards[9]
    elif mode == "very fine":
        r = randint(1, 5)
        if r == 1:
            return "Destroyed"
        else:
            return cards[9]

def upgrade_zn_mng_card(mode):
    if mode == "rough":
        r = randint(1,2)
        if r == 1:
            return cards[0]
        else:
            return cards[1]
    elif mode == "coarse":
        return cards[1]
    elif mode == "1:1":
        return cards[3]
    elif mode == "fine":
        return cards[7]
    elif mode == "very fine":
        r = randint(1, 10)
        if r >= 1 and r < 4:
            return cards[6]
        elif r >= 4 and r < 8:
            return cards[7]
        else:
            return cards[8]

def upgrade_facility_card(mode):
    if mode == "rough":
        return cards[6]
    elif mode == "coarse":
        return cards[5]
    elif mode == "1:1":
        return cards[8]
    elif mode == "fine":
        return cards[9]
    elif mode == "very fine":
        r = randint(1, 5)
        if r == 1:
            return "Destroyed"
        else:
            return cards[9]

def upgrade_CI_card(mode):
    if mode == "rough":
        return cards[3]
    elif mode == "coarse":
        return cards[4]
    elif mode == "1:1":
        return cards[5]
    elif mode == "fine":
        return cards[9]
    elif mode == "very fine":
        r = randint(1, 5)
        if r == 1:
            return "Destroyed"
        else:
            return cards[9]

def upgrade_O5_card(mode):
    if mode == "rough":
        return cards[3]
    elif mode == "coarse":
        r = randint (1, 2)
        if r == 1:
            return cards[7]
        else:
            return cards[5]
    elif mode == "1:1":
        return cards[9]
    elif mode == "fine":
        r = randint(1, 2)
        if r == 1:
            return cards[9]
        else:
            return "Destroyed"
    elif mode == "very fine":
        r = randint(1, 5)
        if r == 1:
            return cards[9]
        else:
            return "Destroyed"

upgrade_card(cards)
upgrade_card(cards)
upgrade_card(cards)
upgrade_card(cards)
upgrade_card(cards)
