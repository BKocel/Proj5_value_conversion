## Nazwa programu: "Konwerter jednostek" <br> Plik zawierający program: "main.py"

#### Opis działania programu:
Użytkownik wybiera, jakie jednostki chcę konwertować:
1. Konwertowanie jednostek wagi
2. Konwertowanie jednostek dystansu
Po czym program karze użytkownikowi podać wartość, wskazać jednostkę podanej wartości, oraz jednostkę docelową. <br>
Po podaniu wyszstkich informacji program wypisuje użytkownikowi przekonwertowaną wartość.

#### Użyte zmienne i ich typy:
1. **opmode** typ *int*, przechowje wybrany przez użytkownika tryb operacji programu;
2. **value** typ *float*, przechowuje wartość podaną przez użytkownika;
3. **intype** typ *int*, przechowuje jednostkę wartości podanej przez użytkownika;
4. **outtype** typ *int* przechowuje jednostkę wartości docelowej;
5. **mvalue** typ *float*, tylko przy obliczeniach dystansu, przechowuje wartość podaną przez użytkownika przekonwertowaną do metrów;
6. **gvalue** typ *float*, tylko przy obliczeniach masy, przechowuje wartość podaną przez użytkownika przekonwertowaną na gramy;
7. **outvalue** typ *float*, przechwuje wartość przekonertowaną do jednostki wwybranej przez użytkownika.

#### Najważniejsze funkcje:
1.  Funkcja ***lenghtcalc*** zawarta w programie, odpowiada za konwertowanie jednostek dystansu;
2.  Funkcja ***weightcalc*** zawarta w programie, odpowiada za konwertowanie jednostek masy.

#### Działanie programu:
Użytkownik wybiera tryb pracy programu (kownertowwanie jednostek odległości lub masy), po czym podaje wartość początkową, jej jednostkę oraz jednostkę docelową, po czym program wypisuje wartość przekonwertowaną do jednostki docelowej.

 ```
Witaj w konwerterze jednostek!
Tryby pracy aplikacji:
1. Konwertowanie wagi
2. Konwertowanie odległości
Wybierz tryb pracy: 1
Podaj wartość do przekonwertowania: 1000
Dostępne jednostki wagi
1. Miliglram (mg)
2. Gram (g)
3. Dekagram (dag)
4. Kilogram (Kg)
5. Tona (T)
6. Uncja (oz.)
7. Funty (lb.)
8. Uncja trojańska (troy oz.)
Wybierz jednostkę  wpisanej wartości: 4
Wybierz jednostkę wartości wypisywanej : 5
```
