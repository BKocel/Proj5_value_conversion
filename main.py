
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
    print("8. Uncja trojańska (troy oz.)")
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
        case 8: gvalue = value * 31.1034768 # troy oz to g
        case _: print("Error") # wrong value handler

    match outtype: # converting grams to output value
        case 1: outvalue = gvalue * 1000        # g to mg
        case 2: outvalue = gvalue               # g to g
        case 3: outvalue = gvalue / 10          # g to dag
        case 4: outvalue = gvalue / 1000        # g to kg
        case 5: outvalue = gvalue / 1000000     # g to T
        case 6: outvalue = gvalue / 28.3495231  # g to oz
        case 7: outvalue = gvalue / 453.59237   # g to lb
        case 8: outvalue = gvalue / 31.1034768  # g to troy oz
        case _: print("Error")# wrong value handler

    return(outvalue)


def lenghtcalc(): # lenght calculations
    value = float(input("Podaj wartość do przekonwertowania: "))
    print("Dostępne jednostki odległości:")
    print("1. mikrony (µ)")
    print("2. milimetr (mm)")
    print("3. centymetr (cm)")
    print("4. decymetr (dm)")
    print("5. metr (m)")
    print("6. kilometr (km)")
    print("7. cal (in)")
    print("8. stopa (ft)")
    print("9. jard (yd)")
    print("10. mila (M)")
    print("11. mila morska (Mn)")
    intype = int(input("Wybierz jednostkę  wpisanej wartości: "))
    outtype = int(input("Wybierz jednostkę wartości wypisywanej : "))

    match intype: # convering input unit to meters
        case 1: mvalue = value / 1000000    # µ to m
        case 2: mvalue = value / 1000       # mm to m 
        case 3: mvalue = value / 100        # cm to m
        case 4: mvalue = value / 10         # dm to m
        case 5: mvalue = value              # m to m
        case 6: mvalue = value * 1000       # km to m
        case 7: mvalue = value * 0.0254     # in to m
        case 8: mvalue = value * 0.3048     # ft to m
        case 9: mvalue = value * 0.9144     # yd to m
        case 10: mvalue = value * 1609.344  # M to m
        case 11: mvalue = value * 1852      # Mn to m
        case _: print("Error") # wrong value handler

    match outtype: # converting meters to output unit
        case 1: outvalue = mvalue * 1000000       # m to µ
        case 2: outvalue = mvalue * 1000          # m to mm
        case 3: outvalue = mvalue * 100           # m to cm
        case 4: outvalue = mvalue * 10            # m to dm
        case 5: outvalue = mvalue                 # m to m
        case 6: mvalue = value / 1000             # m to km
        case 7: mvalue = value / 0.0254           # m to in
        case 8: mvalue = value / 0.3048           # m to ft
        case 9: mvalue = value / 0.9144           # m to yd
        case 10: mvalue = value / 1609.344        # m to M
        case 11: mvalue = value / 1852            # m to Mn
        case _: print("Error")# wrong value handler

    return(outvalue)

def volumecalc(): # volume calculations
    value = float(input("Podaj wartość do przekonwertowania: "))
    print("Dostępne jednostki objętości:")
    print("1. mikrony (µ)")
    
    intype = int(input("Wybierz jednostkę  wpisanej wartości: "))
    outtype = int(input("Wybierz jednostkę wartości wypisywanej : "))

    match intype: # convering input unit to meters
        case 1: mvalue = value / 1000000    # µ to m
     
        case _: print("Error") # wrong value handler

    match outtype: # converting meters to output unit
        case 1: outvalue = mvalue * 1000000       # m to µ

        case _: print("Error")# wrong value handler

    return(outvalue)

# CLI
print("Witaj w konwerterze jednostek!")
print("Tryby pracy aplikacji:")
print("1. Konwersja wagi ")
print("2. Konwersja odległości")
print("3. Konwersja obiętości # TODO")
opmode = int(input("Wybierz tryb pracy: "))

match opmode:
    case 1: print(weightcalc())
    case 2: print(lenghtcalc())
    case 3: print(volumecalc())
    case _: print("Error")