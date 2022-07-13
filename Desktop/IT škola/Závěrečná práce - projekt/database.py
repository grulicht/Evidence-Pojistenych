import sqlite3


VYTVORENI_EVIDENCE_POJISTENYCH_TABLE = "CREATE TABLE IF NOT EXISTS evidence_pojistenych (id INTEGER PRIMARY KEY, Jmeno TEXT, Prijimeni TEXT, Vek INTEGER, Telefoni_cislo INTEGER);"

PRIDANI_POJISTENEHO = "INSERT INTO evidence_pojistenych (Jmeno, Prijimeni, Vek, Telefoni_cislo) VALUES (?, ?, ?, ?);"

VYPSANI_SEZNAMU_PPOJISTENYCH = "SELECT * FROM evidence_pojistenych;"

VYHLEDANI_POJISTENEHO_PODLE_JMENA_A_PRIJIMENI = "SELECT * FROM evidence_pojistenych WHERE Jmeno = $Jmeno AND Prijimeni = $Prijimeni;"

VYMAZANI_POJISTENEHO = "DELETE FROM evidence_pojistenych WHERE Jmeno = $Jmeno AND Prijimeni = $Prijimeni;"


def connect():
    return sqlite3.connect("data.db")

def vytvoreni_tabulky(connection):
    with connection:
        connection.execute(VYTVORENI_EVIDENCE_POJISTENYCH_TABLE)

def pridani_noveho_pojisteneho (connection, Jmeno, Prijimeni, Vek, Telefoni_cislo):
    with connection:
        connection.execute (PRIDANI_POJISTENEHO, (Jmeno, Prijimeni, Vek, Telefoni_cislo))

def vypsani_seznamu_pojistenych(connection):
    with connection:
        return connection.execute(VYPSANI_SEZNAMU_PPOJISTENYCH).fetchall()

def vyhledani_pojisteneho_podle_jmena_a_prijimeni(connection, Jmeno, Prijimeni):
    with connection:
        return connection.execute(VYHLEDANI_POJISTENEHO_PODLE_JMENA_A_PRIJIMENI, (Jmeno, Prijimeni)).fetchall()

def vymazani_pojisteneho_podle_jmena_a_prijimeni(connection, Jmeno, Prijimeni):
    with connection:
        return connection.execute(VYMAZANI_POJISTENEHO, (Jmeno, Prijimeni)).fetchall()




