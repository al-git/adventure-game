import time
import random


def narrate(*script):
    for i in range(len(script)):
        print(script[i])
        time.sleep(1)


def choices(*options):
    dictionary = dict(options)
    keys = list(dictionary.keys())
    consequences = list(dictionary.values())
    print('\n Please enter the number of your choice:')
    for i in range(len(keys)):
        print(str(i+1) + '. ' + keys[i])
    choice = input()
    try:
        if int(choice) - 1 in range(len(keys)):
            choice = int(choice) - 1
            if callable(consequences[choice]):
                consequences[choice]()
            else:
                print(consequences[choice])
                time.sleep(1)
                choices(*options)
        else:
            print("Sorry, that's not a valid option. Please try again.")
            time.sleep(1)
            choices(*options)
    except ValueError:
        print("Sorry, that's not a valid option. Please try again.")
        time.sleep(1)
        choices(*options)


def door():
    narrate(
        'You open the door and find yourself in a kitchen.',
        'Before you is a small table draped with a checkerboard cloth and '
        'laden with two plates.',
        'One plate bears two jellybeans and the other, '
        'two pieces of chocolate.',
        'Which do you choose?'
    )
    choices(
        ('Jellyeans', sleep),
        ('Chocolate', victory)
    )


def sleep():
    narrate(
        'The jellybeans taste sweet. You feel a sudden burst of energy'
        ' followed by an intense need to take a nap.',
        'You head back to the room where you started, lie down, and go back '
        'to sleep.'
        '\nGame over :('
    )


def victory():
    narrate(
        'You eat one piece of chocolate, feeling a warm glow in your stomach.',
        'You eat the second and feel your intellectual capabilities expanding'
        ' faster than the speed of light.',
        'You crouch and leap off the floor, flying through the ceiling '
        'and soar above the countryside.',
        'Over the next five years, you manage to solve the global economic '
        'crisis, retire in Tahiti, and live happily ever-after.',
        'You win!'
    )


def play():
    narrate(
        '"Wake up"',
        '...',
        'The sound of leaves clapping in the breeze stirs you from sleep.',
        'You rub your eyes and open them slowly.',
        'You peer around the room and see a book, a door, and a window.',
        'What do you do?'
    )
    choices(
        ('Pick up the book', 'The title of the book is: Chocolate. '
            'Feeling hungry, you put it down.'
            '\n What would you like to do now?'),
        ('Open the door', door),
        ('Look out the window', 'You peer out the window and see a tree '
            'adorned with ' + str(random.randint(0, 100)) + ' '
            + random.choice(['singing bluejays', 'humming warblers']) +
            '. Their song makes you smile.'
            '\n What would you like to do now?')
    )


def replay():
    print("\n Would you like to play again? \n")
    choices(
        ("Yes, I'd like to play again.", again),
        ("No thank you.", done)
    )


def again():
    print("OK, here we go!")
    play()


def done():
    print("OK, thank you for playing!")
    exit()


play()
replay()
