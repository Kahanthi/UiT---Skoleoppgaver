import calendar

January = ("Januar")
Febuary = ("Februar")
March = ("Mars")
May = ("Mai")
June = ("Juni")
July = ("Juli")
October = ("Oktober")
December = ("Desember")


# Prompt user to enter year
year = int(input("Skriv inn et årstall: "))

# Prompt user to enter month
month = int(input("Skriv inn en måned (benytt 1-12): "))

# Check if valid input
if 1 <= month <= 12 and year > 0:
    # Fnd days in month
    days_in_month = calendar.monthrange(year, month)[1]

    # Display result
    print(f"I {calendar.month_name[month]} år {year}, er/var det {days_in_month} dager.")
else:
    print("Ugyldig inndata. Vennligst skriv inn gyldig år (f.eks. 2000) og måned (1-12).")




