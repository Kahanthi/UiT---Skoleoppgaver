# Prompt the user to enter a three-digit integer
user_input = input("Skriv inn et tre-siffret heltall (eks. 100, 340, 721 etc.): ")

# Check if the input is a valid three-digit integer
if user_input.isdigit() and len(user_input) == 3:
    # Reverse the input
    reversed_input = user_input[::-1]


    # Check if the reversed input is equal to the original input
    if user_input == reversed_input:
        print(f"{user_input} er et palindromsk tall!.")
    else:
        print(f"{user_input} Dette er ikke et palindromsk tall.")
else:
    print("Feil, husk å bruke et heltall som består av tre siffer")