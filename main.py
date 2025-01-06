
# operating modes
def weightcalc(): # weight calculations
    value = float(input("Podaj wartość do przekonwertowania: "))
    print("Dostępne jednostki wagi")
    print("1. Miliglram (mg)")
    print("2. Gram (g)")
    print("3. Dekagram (dag)")
    print("4. Kilogram (Kg)")
    print("5. Tona (T)")
    print("6. Uncja (oz.)")
    print("7. Funty (lb.)")
    intype = int(input("Wybierz jednostkę  wpisanej wartości: "))
    outtype = int(input("Wybierz jednostkę wartości wypisywanej : "))

    match intype: # convering input value to grams
        case 1: gvalue = value / 1000       # mg to g
        case 2: gvalue = value              # g to g
        case 3: gvalue = value * 10         # dag to g
        case 4: gvalue = value * 1000       # kg to g
        case 5: gvalue = value * 1000000    # T to g
        case 6: gvalue = value * 28.3495231 # oz to g
        case 7: gvalue = value * 453.59237  # lb to g
        case _: print("Error") # wrong value handler

    match outtype: # converting grams to output value
        case 1: outvalue = gvalue * 1000        # g to mg
        case 2: outvalue = gvalue               # g to g
        case 3: outvalue = gvalue / 10          # g to dag
        case 4: outvalue = gvalue / 1000        # g to kg
        case 5: outvalue = gvalue / 1000000     # g to T
        case 6: outvalue = gvalue / 28.3495231  # g to oz
        case 7: outvalue = gvalue / 453.59237   # g to lb
        case _: print("Error")# wrong value handler

    print(outvalue)


def lenghtcalc(): # lenght calculations
    print("Dostępne jednostki odległości")

# CLI
print("Witaj w konwerterze jednostek!")
print("Tryby pracy aplikacji:")
print("1. Konwersja wagi ")
print("2. Konwersja odległości")
print("3. Konwersja obiętości")
opmode = int(input("Wybierz tryb pracy: "))

match opmode:
    case 1: weightcalc()
    case 2: lenghtcalc()
    case _: print()