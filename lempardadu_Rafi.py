import random

dice = {}
def roll(sides=6):
    lempardadu = random.randint(1,sides)
    return lempardadu



def main():
    play = True
    while play:
        angka = roll()
        pilihan = input('Roll Dice? (y/n)')
        if pilihan.lower() != "n":
            if angka in dice:
                dice[angka] += 1
            else:
                dice[angka] = 1
            print('Angka yang didapat : ', angka)
        else:
            play = False
            for angka in range(1,7):
                print("Angka", str(angka), "keluar", str(dice[angka]), "kali.")

main()