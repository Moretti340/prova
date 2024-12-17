import es011 as clc
while True:
    print("benvenuto nella nostra calcolatrice")
    print("inserisci la operazione che vuoi effettuare ")
    scelta = int(input("1 sottrazione 2 addizione 0 per uscire "))
    if scelta==0:
        break
    elif scelta==1:
        clc.sottrazione()
    
    elif scelta==2:
        clc.somma()
    else:
        print("Scelta non corretta!")
