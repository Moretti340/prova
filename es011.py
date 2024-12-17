while True:
    print("benvenuto nella nostra calcolatrice")
    print("inserisci la operazione che vuoi effettuare ")
    scelta = int(input("1 sottrazione 2 addizione "))
    if scelta==0:
        break
    elif scelta==1:
        n1=int(input("inserisci il primo numero "))
        n2=int(input("inserisci il secondo numero "))
        diff=n1-n2
        print("la differenza e ",diff)
    
    elif scelta==2:
        n1=int(input("inserisci il primo numero "))
        n2=int(input("inserisci il secondo numero "))
        diff=n1+n2
        print("la somma e ",diff)
    else:
        print("Scelta non corretta!")
