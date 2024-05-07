# Funktion zur Berechnung des EBCED-Werts eines arabischen Buchstabens
def buchstabenwert(buchstabe):
    #die werte wurden aus der Seite https://sorularlaislamiyet.com/blog/ebced-hevvez-hutti-ve-rastgelelik genommen.
    buchstaben_werte = {
        'ا': 1, 'ب': 2, 'ت': 400, 'ث': 500, 'ج': 3, 'ح': 8, 'خ': 600, 'د': 4, 'ذ': 700, 'ر': 200,
        'ز': 7, 'س': 60, 'ش': 300, 'ص': 90, 'ض': 800, 'ط': 9, 'ظ': 900, 'ع': 70, 'غ': 1000,
        'ف': 80, 'ق': 100, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'ه': 5, 'و': 6, 'ي': 10
    }
    return buchstaben_werte.get(buchstabe, 0)  # Wenn der Buchstabe nicht gefunden wird, gib 0 zurück

# Eingabe des Wortes
eingabe = input("Geben Sie ein Wort ein: ")

# Berechnung und Ausgabe der Summe der EBCED-Werte des eingegebenen Wortes
print("Die Summe der EBCED-Werte des Wortes '{}' beträgt: {}".format(eingabe, sum(buchstabenwert(buchstabe) for buchstabe in eingabe)))
