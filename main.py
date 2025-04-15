import mariadb
import sys
 
#connect mariadb
 
try:
    conn = mariadb.connect(
        user = "na_ng",
        password = "botanical",
        host = "127.0.0.1",
        port = 3307,
        database = "schlumpfshop3")
 
except mariadb.Error as e:
    print(f"Error connecting to MariaDB PLatform: {e}")
    sys.exit(1)
 
#get cursor
 
cur = conn.cursor()

min_anzahl = int(input("Geben Sie die Mindeststückzahl ein: "))

cur.execute(
    "SELECT artikel.Artikelname, artikel.Lagerbestand, lieferant.Lieferantenname FROM artikel INNER JOIN lieferant ON artikel.Lieferant = lieferant.ID_Lieferant WHERE artikel.Lagerbestand <?", (min_anzahl,))


for (artikel, lagerbestand, lieferant) in cur:
    #if lagerbestand < min_anzahl:
        print(f"{lieferant} {artikel}: {lagerbestand} St.")

