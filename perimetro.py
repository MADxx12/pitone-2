print("Benvenuto nel calcolatore del perimetro! ")
forma = int( input ("Premi 1 per quadrato, 2 per cerchio, 3 per rettangolo: "))
if forma == 1 :
    perimetro_q= float( input ("Inserisci la lunghezza del lato: "))
    calcolo_q= perimetro_q * 4
    print("Il perimetro del tuo quadrato e' di: ", calcolo_q )
    
elif forma == 2 :
        raggio_c= float( input ("Inserisci il raggio del cerchio: "))
        pi_greco = 3.14
        calcolo_c= 2 * pi_greco * raggio_c 
        print("La circonferenza del tuo cerchio e' di: ", calcolo_c )
elif forma == 3 :
     base_r= float( input ("Inserisci la lunghezza della base: "))
     altezza_r= float( input ("Inserisci la lunghezza dell' altezza: "))
     calcolo_r= (base_r * 2 + altezza_r * 2)
     print("Il perimetro del tuo rettangolo e' di: ", calcolo_r )
else:
      print("Non hai selezionato uno dei tre numeri richiesti, il computer si autodistruggera' in 10 secondi")
     
    

    


