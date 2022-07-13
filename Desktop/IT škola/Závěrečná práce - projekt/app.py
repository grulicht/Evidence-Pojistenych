import database

MENU = """
-----------------------------
EVIDENCE POJIŠTĚNÝCH
-----------------------------

Vyberte si akci:

1 - Přidat nového pojištěného
2 - Vypsat všechny pojištěné
3 - Vyhledat pojištěného
4 - Vymazat pojištěného
5 - Konec

Vaše akce:"""

def menu():
    connection = database.connect()
    database.vytvoreni_tabulky(connection)

    while (user_input := input(MENU)) != "5":
        if user_input == "1":
            Jmeno = input ("Zadej jméno pojištěného:\n")
            Prijimeni = input("Zadej přijímení pojištěného:\n")
            Vek = int(input("Zadej věk pojištěného:\n"))
            Telefoni_cislo = int(input("Zadej telefoní číslo pojištěného:\n +420"))
            
            database.pridani_noveho_pojisteneho(connection, Jmeno, Prijimeni, Vek, Telefoni_cislo)

            input("Data byla uložena, pokračujte libovolnou klavesou...")
            continue

        elif user_input == "2":
            pojisteni = database.vypsani_seznamu_pojistenych(connection)

            for pojisteny in pojisteni:
                print(f"{pojisteny [0]} {pojisteny[1]} {pojisteny[2]} {pojisteny[3]} {pojisteny[4]}")

            input("Zde vidíte výpis pojištěných. Pokud se žádné data nevypsaly, žádný pojištěný zde není. Pokračujte libovolnou klavesou...")
            continue
        

        elif user_input == "3":
            Jmeno = input("Zadej jméno pojištěného:\n")
            Prijimeni = input("Zadej přijímení pojištěného:\n")
            pojisteni = database.vyhledani_pojisteneho_podle_jmena_a_prijimeni(connection, Jmeno, Prijimeni)

            pojisteny = False
            for pojisteny in pojisteni:
                if pojisteny in pojisteni:
                    pojisteni = True
            if pojisteni:
                print(f"{pojisteny [0]} {pojisteny[1]} {pojisteny[2]} {pojisteny[3]} {pojisteny[4]}")
                input("Pojištěný nalezen, pokračujte libovolnou klavesou...")
            else:
                input("Pojištěný nenalezen! Pokračujte libovolnou klavesou...")
                continue

        elif user_input == "4":
            Jmeno = input("Zadej jméno pojištěného:\n")
            Prijimeni = input("Zadej přijímení pojištěného:\n")
            pojisteni = database.vymazani_pojisteneho_podle_jmena_a_prijimeni(connection, Jmeno, Prijimeni)

            pojisteny = False
            for pojisteny in pojisteni:
                if pojisteny in pojisteni:
                    pojisteni = True
            continue
        
        elif user_input == "5":
            pass

        else:
            input("Nevyhovující akce, zkuste to znovu! Pokračujte libovolnou klávesou...")
        continue
            
menu()
