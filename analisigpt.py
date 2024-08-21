import re

def conta_parole(testo):
    # Converto il testo in minuscolo
    testo = testo.lower()
    
    # Rimuovo la punteggiatura usando una regex
    testo = re.sub(r'[^\w\s]', '', testo)
    
    # Divido il testo in parole
    parole = testo.split()
    
    # Conto le occorrenze delle parole usando un dizionario
    conteggio = {}
    for parola in parole:
        conteggio[parola] = conteggio.get(parola, 0) + 1
    
    return conteggio


testo = "Ciao, ciao! Come stai? Stai bene? no! STAI USANDO chatgpt? NO..."
output = conta_parole(testo)
print(output)  
