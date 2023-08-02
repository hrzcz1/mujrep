"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Martin Harazin
email: martinharazin8@gmail.com
discord: Martin H.#1050
"""

import random
def random_cislo(): 
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4])) 


def pocet_bulls_and_cows(gen_cislo, tip):
    bulls = 0
    cows = 0
    for i in range(len(gen_cislo)):
        if gen_cislo[i] == tip[i]:
            bulls += 1
        elif gen_cislo[i] in tip:
            cows += 1
    return bulls, cows

def bulls_and_cows():
    gen_cislo = random_cislo()
    print("Ahoj!")
    print("-" * 70)
    print("Tento program vygeneruje náhodné 4 místné číslo, které je nutno uhádnout.\nZahrajme si hru Bulls And Cows!!")
    print("-" * 70)
    print(gen_cislo) #použito pro  zobrazení generovaného čísla pro test bulls/cows
    pokus = 0
    while True:
        pokus += 1
        tip = input("Zadej číslo: ")
        print("-" * 50)

        if len(tip) != 4:
            print("Zadej 4 místné číslo: ")
            pokus -= 1
            print("Pokus:", pokus)
            print("-" * 50)
            continue
            
        bulls, cows = pocet_bulls_and_cows(gen_cislo, tip)
        if bulls == 1:
            bulls_str = "Bull"
        else:
            bulls_str = "Bulls"
        if cows == 1:
            cows_str = "Cow"
        else:
            cows_str = "Cows"

        print(f"{bulls} {bulls_str}, {cows} {cows_str}, Pokus: {pokus}")
        
        if tip == gen_cislo:
            
            if pokus == 1:
                pokus_str = "pokus"
            elif pokus >=1 and pokus <= 4:
                pokus_str = "pokusy"
            else:
                pokus_str = "pokusů"

            print(f"Bravo, potřeboval jsi na to {pokus} {pokus_str}.")
            print("-" * 50)

            break


            
bulls_and_cows()