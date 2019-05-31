import time
while True:
    print('''
    Calcolatore!
    by Beard Developer
    www.bearddeveloper.it
    Opzioni:


    - Addizione, seleziona a;
    - Sottrazione, seleziona b;
    - Moltiplicazione, seleziona c;
    - Divisone, seleziona d;
    - Calcolo esponenziale, seleziona e;
    - Calcolo area di un rettangolo, seleziona f;
    - Calcolo area cerchio con il raggio, seleziona g;
    - Calcolo area triangolo, seleziona h;
    - Calcolo area trapezio, seleziona i;
    - Per uscire digitare ESC;
    ''')

    scelta = input('Inserisci l\'opzione desiderata --->  ')
    if scelta == "a":
        print('\nHai scelto: Addizione\n')
        a = float(input('Inserisci il Primo Numero -> '))
        b = float(input('Inserisci il Secondo Numero -> '))
        print('Il risultato è: ' + str(a + b))
    elif scelta == "b":
        print('\nHai Scelto: Sottrazione\n')
        a = float(input('Inserisci il Primo Numero -> '))
        b = float(input('Inserisci il Secondo Numero -> '))
        print('Il risultato è: ' + str(a - b))
    elif scelta == "c":
        print('\nHai scelto: Moltiplicazione\n')
        a = float(input('Inserisci il Primo Numero -> '))
        b = float(input('Inserisci il Secondo Numero -> '))
        print('Il risultato è: ' + str(a * b))
    elif scelta == "d":
        print('\nHai scelto: Divisione\n')
        a = float(input('Inserisci il Primo Numero -> '))
        b = float(input('Inserisci il Secondo Numero -> '))
        print('Il risultato è: ' + str(a / b))
    elif scelta == "e":
        print('\nHai scelto: Calcolo esponenziale\n')
        a = float(input('Inserisci la Base -> '))
        b = float(input('Inserisci l\'Esponente -> '))
        print('Il risultato è: ' + str(a ** b))
    elif scelta == "f":
        print('\nHai scelto: Calcolo area di un rettangolo\n')
        a = float(input("Aggiungi la misura della BASE -> "))        
        b = float(input("Aggiungi la misura dell'ALTEZZA -> "))
        print('Il risultato è: ' + str(a * b))
    elif scelta == "g":
        print("Hai scelto: Area cerchio")
        r = float(input('Inserisci il valore del raggio -> '))
        print(f"L'Area del Cerchio, avente raggio {r} è: {(r * r) * 3.14}")
    elif scelta == "h":
        print('\nHai scelto: Area triangolo\n')
        a = float(input("Aggiungi la misura della base ->"))
        b = float(input("Aggiungi la misura dell'altezza ->"))
        print('Il risultato è: ' + str(a*b/2))
    elif scelta == "i":
        print('\nHai scelto: Area trapezio\n')
        a = float(input("Aggiungi la misura della BASE MINORE ->"))
        b = float(input("Aggiungi la misura della BASE MAGGIORE ->"))
        c = float(input("Aggiugni la misura dell'ALTEZZA ->"))
        print('Il risultato è: ' + str((a+b)*c/2))
    elif scelta == "ESC":
        print('''L'applicazione verrà ora chiusa!


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        break


    loop = input('\nDesideri continuare ad usare l\'applicazione? S/N ')
    if loop == "S" or loop == "s":
        print('''Menù principale


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        continue
    else:
        print('''Grazie, alla prossima.


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        break
