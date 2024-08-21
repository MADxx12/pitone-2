def calcola_media_mobile(numeri, n):
    medie_mobili = []
    for i in range(len(numeri)):
        sezione_corrente = numeri[max(0, i - n + 1):i + 1]
        media = sum(sezione_corrente) / len(sezione_corrente)
        medie_mobili.append(media)
    return medie_mobili


numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 6
output = calcola_media_mobile(numeri, n)
print(output)  
