n = int(input("skriv inn et tall mellom 0-15: "))
l = list()

if 0 <= n <= 15:
    original_n = n
    while n != 0:
        r = n % 2
        l.append(r)
        n = n // 2

    l.reverse()

    binary_str = ''.join(map(str, l))
    print(f"Det binære tallet for {original_n} er {binary_str}")
else:
    print("Ugyldig tall. Vennligst skriv inn et tall mellom 0 og 15.")


#Måten denne koden virker er at den tar simpel logikk og endrer alle tall til binære tall
#Kilde = Revel og en inder på youtube: "DECIMAL TO BINARY NUMBER CONVERSION PROGRAM IN PYTHON || DECIMAL TO BINARY || PYTHON PROGRAMMING"
#Forskjellen mellom denne koden og videoen er at denne viser det binære tallet bedre enn hva som kom opp på videoen, ved bruk av streng-funksjon
