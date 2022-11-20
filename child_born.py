import sqlite3
import random

# kapcsolódik a members adatbázishoz
conn = sqlite3.connect("members.db")
# példányosítja a cursor-t
curs = conn.cursor()
# létrehoz egy táblát ha nem létezik
curs.execute(
    "CREATE TABLE IF NOT EXISTS members(Name TEXT, Vitality INTEGER, Resilience INTEGER, PossibleChildNumber INTEGER, ChildNumber INTEGER, Balance INTEGER, Position TEXT, Alive BOOLEAN, FatherId INTEGER)")

# az elején létrehozza a genesis-t
curs.execute("INSERT INTO members VALUES ('Ősapa', 15, 15, 2, 0, 300, 'Paraszt', True, 0)")

# utód létrehozása
def born():
    # apa azonosítóját lekéri
    father = input("FatherID: ")

    # lekéri a lehetséges gyerekeinek a számát
    curs.execute("SELECT PossibleChildNumber FROM members WHERE ROWID = ?", (father))
    get_possible_child_number = curs.fetchone()
    for possible_child_number in get_possible_child_number:
        possible_child_number
    # lekéri a gyerekeinek a számát
    curs.execute("SELECT ChildNumber FROM members WHERE ROWID = ?", (father))
    get_child_number = curs.fetchone()
    for child_number in get_child_number:
        child_number
    # lekéri hogy él-e az apa
    curs.execute("SELECT Alive FROM members WHERE ROWID = ?", (father))
    get_alive = curs.fetchone()
    for alive in get_alive:
        alive

    # Ha már elérte az apa a gyerek limitet akkor nem hajtja végbe
    if child_number < possible_child_number and alive == 1:
        # utód nevét lekéri
        name = input("Utód neve: ")
        # lekéri az apa vitality értékét
        curs.execute("SELECT Vitality FROM members WHERE ROWID = ?", (father))
        get_vitality = curs.fetchone()
        for vitality in get_vitality:
            # 3/-3
            vitality += random.randrange(-3, 4)
        # lekéri az apa resiliance értékét
        curs.execute("SELECT Resilience FROM members WHERE ROWID = ?", (father))
        get_resilience = curs.fetchone()
        for resilience in get_resilience:
            # 3/-3
            resilience += random.randrange(-3, 4)
        # lekéri az apa possiblechild értékét
        curs.execute("SELECT PossibleChildNumber FROM members WHERE ROWID = ?", (father))
        get_possible_child_number = curs.fetchone()
        for possible_child_number in get_possible_child_number:
            # 1/-1
            possible_child_number += random.randrange(-1, 3)
        # lekéri az apa tisztségét
        curs.execute("SELECT Position FROM members WHERE ROWID = ?", (father))
        get_position = curs.fetchone()
        for position in get_position:
            position
        # létrehozza az utódot a váltotzatott paraméterekkel
        curs.execute("INSERT INTO members VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, vitality, resilience, possible_child_number, 0, 0, position, True, father))
        curs.execute("UPDATE members SET ChildNumber = ChildNumber + 1 WHERE ROWID = ?", (father))

    else:
        print("Maximális gyerek limit elérve")
while True:
    born()
    conn.commit()

