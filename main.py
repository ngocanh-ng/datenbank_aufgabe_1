import mariadb
import sys

import tkinter as tk
from tkinter import ttk
 
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

#class

class Artikel:
    def __init__(self, artikelname, preis_netto, lagerbestand, lieferantname):
        self.name = artikelname
        self.preis = preis_netto
        self.bestand = lagerbestand
        self.lieferant = lieferantname
    def values(self):
        return (self.name, self.preis, self.bestand, self.lieferant)
    
# get cursor
 
abfrage = conn.cursor()
query = "SELECT artikel.Artikelname, artikel.Preis_Netto, artikel.Lagerbestand, lieferant.Lieferantenname FROM artikel INNER JOIN lieferant ON artikel.Lieferant = lieferant.ID_Lieferant"
abfrage.execute(query)

artikel_liste = []

for row in abfrage:
    artikel = Artikel(*row)
    artikel_liste.append(artikel.values())

# Functions

def filtern():
    for row in tree.get_children():
        tree.delete(row)
    try:
        menge = int(entry_menge.get())
    except ValueError:
        menge = 0

    for artikel in artikel_liste:
        if artikel[2] < menge:  
            tree.insert("", "end", values=artikel)

# Tkinter

root = tk.Tk()
root.title("Artikelabfrage")
root.geometry("900x600")

label_menge = tk.Label(root, text = "Mindestmenge:")
label_menge.pack()

entry_menge = ttk.Entry(root)
entry_menge.pack()
menge = entry_menge.get()

button_filtern = ttk.Button(
    root,
    text = "Filtern",
    command = filtern
)
button_filtern.pack()

columns = ("Artikelname", "Preis", "Lagerbestand", "Lieferant")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)  
    tree.column(col, anchor="center", width=140)
tree.pack(expand=True, fill="both")

root.mainloop()