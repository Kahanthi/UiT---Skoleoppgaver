user_input = input("Skriv inn 9 enkelttall: ")
if len(user_input) != 9 or not user_input.isdigit():
    print("Feil inndata. Vennligst skriv inn nøyaktig 9 siffer.")

ISBN = 0
for i in range(0, 9):
    ISBN += int(user_input[i]) * (i+1)
d10 = ISBN % 11
if d10 == 10:
    d10 = "X"

print (f'Ditt ISBN er {user_input}{d10}')
