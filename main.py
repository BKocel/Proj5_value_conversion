
# operating modes
def weightcalc(): # weight calculations
    value = float(input("Podaj wartość do przekonwertowania"))
    print("Dostępne jednostki wagi")
    print("1. Miliglram (mg)")
    print("2. Gram (g)")
    print("3. Dekagram (dag)")
    print("4. Kilogram (Kg)")
    print("5. Tona (T)")
    print("6. Uncja (oz.)")
    print("7. Funty (lb.)")
    intype = int(input("Wybierz typ wpisanej wartości: "))
    outtype = int(input("Wybierz typ wypisanej wartości: "))


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