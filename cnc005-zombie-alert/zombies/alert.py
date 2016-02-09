from zombies.being import Being
from time import sleep


max_coord = 25

def display_beings(beings):
    print("#" * (max_coord + 2))
    for x in range(0, max_coord):
        print("#", end="")
        for y in range(0, max_coord):

            display_as = " "
            for being in beings:
                if being.x == x and being.y == y:
                    display_as = being.reveal()

            print(display_as, end="")
        print("#")
    print("#" * (max_coord + 2))
    print("")

def has_humans(beings):
    i = 0
    upper = len(beings)
    human_found = False

    while i < upper and not human_found:
        human_found = (beings[i].reveal() == "H")
        i += 1

    return human_found

def move(beings):
    for x in beings:
        x.move()

def attack(zombies, humans):
    for zombie in zombies:
        zombie.move_toward(humans)

def humans_at(x, y, beings):
    return [being for being in beings if being.reveal() == "H" and being.at(x,y)]

def get_zombies(beings):
    return [being for being in beings if being.reveal() == "Z"]

def get_humans(beings):
    return [being for being in beings if being.reveal() == "H"]

def separate(beings):
    zombies = get_zombies(beings)
    humans = get_humans(beings)
    return zombies, humans

def start():
    beings = []

    for x in range(0, max_coord):
        human = Being(max_coord)
        human.locate()
        beings.append(human)

    zombie = Being(max_coord)
    zombie.zombify()
    zombie.locate()
    beings.append(zombie)

    while has_humans(beings):
        zombies, humans = separate(beings)
        move(humans)
        attack(zombies, humans)

        for zombie in zombies:
            victims = humans_at(zombie.x, zombie.y, humans)
            for victim in victims:
                victim.zombify()

        display_beings(beings)
        sleep(0.1)
