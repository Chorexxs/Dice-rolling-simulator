# Programa que tira los dados de manera aleatoria

# Primero se importa random y se crea la función de tirar los dados

import random


def roll_dice():

    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }

# Luego se crea la variable de roll para permitir que el usuario tire los dados

# Se usa random.randit para tirar los dados del 1 al 6

    roll = input("¿Tirar dados? (Si/No) : ")
    while roll.lower() == "Si". lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Tus dados son: {} y {}". format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("¿Tirar otra vez? (Si/No): ")

# Por último se llama a la función para ejecutarla


roll_dice()
