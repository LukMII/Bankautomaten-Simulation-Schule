import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import time

# Definieren der globalen Variablen
# Die PIN des Benutzers
pin = "1234"
# Zählt die Anzahl der fehlerhaften PIN-Eingaben
counter = 0
# Die maximale Anzahl an fehlerhaften Versuchen
limit = 3
# Anfangsguthaben des Benutzers
balance = 6000000
transaction_history = []

# Sicherheitsschlüssel
security_key = None

# Farben definieren
# Hintergrundfarbe
background_color = "#B0C4DE"
# Buttonfarbe
button_color = "#1E90FF"
# Textfarbe
text_color = "#000000"        

# Funktion zur Anzeige des Hauptmenüs
def display_main_menu():
    global pin_entry, pin_change_window

    # Erstellen des Hauptmenü-Fensters
    main_menu_window = tk.Tk()
    main_menu_window.title("Hauptmenü")
    # Hintergrundfarbe einstellen
    main_menu_window.configure(bg=background_color)  

    # Label zur Begrüßung des Benutzers
    label = tk.Label(main_menu_window, text="Willkommen bei der Walldürner Bank!", font=("Arial", 16), bg=background_color, fg=text_color)
    label.pack(pady=20)

    # Funktion zur Anzeige des Kontostands
    def show_balance():
        messagebox.showinfo("Kontostand", f"Ihr aktueller Kontostand beträgt: {balance} €")

    # Funktion zum Abheben von Geld
    def withdraw():
        # Funktion zum Abheben des Geldes
        def withdraw_money():
            global balance
            withdraw_amount = int(withdraw_entry.get())
            if withdraw_amount > 50000 or withdraw_amount > balance:
                messagebox.showwarning("Warnung", "Abhebungslimit überschritten oder nicht genügend Guthaben.")
            elif withdraw_amount % 10 != 0:
                messagebox.showwarning("Warnung", "Bitte geben Sie einen Betrag ein, der durch 10 teilbar ist.")
            else:
                balance -= withdraw_amount
                transaction_history.append(f"Abhebung: -{withdraw_amount} €")
                messagebox.showinfo("Erfolgreich", f"Sie haben erfolgreich {withdraw_amount} € abgehoben. Ihr aktueller Kontostand beträgt: {balance} €")
                withdraw_window.destroy()

        # Erstellen des Abhebefensters
        withdraw_window = tk.Toplevel(main_menu_window)
        withdraw_window.title("Abheben")
        # Hintergrundfarbe einstellen
        withdraw_window.configure(bg=background_color)  

        # Label und Eingabefeld für den Betrag
        label = tk.Label(withdraw_window, text="Bitte geben Sie den Betrag ein, den Sie abheben möchten:", font=("Arial", 12), bg=background_color, fg=text_color)
        label.pack(pady=10)
        withdraw_entry = tk.Entry(withdraw_window, font=("Arial", 12), width=20)
        withdraw_entry.pack(pady=10)

        # Button zum Abheben
        withdraw_button = tk.Button(withdraw_window, text="Abheben", font=("Arial", 12), command=withdraw_money, bg=button_color, fg=text_color)
        withdraw_button.pack(pady=10)

    # Funktion zum Einzahlen von Geld
    def deposit():
        # Funktion zum Einzahlen des Geldes
        def deposit_money():
            global balance
            deposit_amount = int(deposit_entry.get())
            balance += deposit_amount
            transaction_history.append(f"Einzahlung: +{deposit_amount} €")
            messagebox.showinfo("Erfolgreich", f"Sie haben erfolgreich {deposit_amount} € eingezahlt. Ihr aktueller Kontostand beträgt: {balance} €")
            deposit_window.destroy()

        # Erstellen des Einzahlungsfensters
        deposit_window = tk.Toplevel(main_menu_window)
        deposit_window.title("Einzahlen")
        # Hintergrundfarbe einstellen
        deposit_window.configure(bg=background_color)  

        # Label und Eingabefeld für den Betrag
        label = tk.Label(deposit_window, text="Bitte geben Sie den Betrag ein, den Sie einzahlen möchten:", font=("Arial", 12), bg=background_color, fg=text_color)
        label.pack(pady=10)
        deposit_entry = tk.Entry(deposit_window, font=("Arial", 12), width=20)
        deposit_entry.pack(pady=10)

        # Button zum Einzahlen
        deposit_button = tk.Button(deposit_window, text="Einzahlen", font=("Arial", 12), command=deposit_money, bg=button_color, fg=text_color)
        deposit_button.pack(pady=10)

    # Funktion zur Anzeige der letzten Transaktionen
    def show_transaction_history():
        # Die letzten 5 Transaktionen anzeigen
        transaction_str = "\n".join(transaction_history[-5:])  
        messagebox.showinfo("Letzte Transaktionen", f"Ihre letzten Transaktionen:\n{transaction_str}")

    # Funktion zur Änderung der PIN
    def change_pin():
        global pin
        new_pin = pin_entry.get()
        if len(new_pin) != 4 or not new_pin.isdigit():
            messagebox.showwarning("Warnung", "Die neue PIN muss 4-stellig sein und nur aus Zahlen bestehen.")
        else:
            pin = new_pin
            messagebox.showinfo("Erfolgreich", "Die PIN wurde erfolgreich geändert.")
            pin_entry.delete(0, tk.END)
            if pin_change_window:
                pin_change_window.destroy()

    # Funktion zum Anzeigen des PIN-Änderungsfensters
    def show_change_pin_window():
        global pin_entry, pin_change_window
        pin_change_window = tk.Toplevel(main_menu_window)
        pin_change_window.title("PIN Änderung")
        pin_change_window.configure(bg=background_color)
        
        # Hintergrundfarbe einstellen
        label = tk.Label(pin_change_window, text="Bitte geben Sie Ihre neue PIN ein:", font=("Arial", 12), bg=background_color, fg=text_color)
        label.pack(pady=10)

        pin_entry = tk.Entry(pin_change_window, font=("Arial", 12), show="*", width=20)
        pin_entry.pack(pady=10)

        submit_button = tk.Button(pin_change_window, text="Bestätigen", font=("Arial", 12), command=change_pin, bg=button_color, fg=text_color)
        submit_button.pack(pady=10)

    # Funktion zum Beenden des Programms
    def quit_program():
        main_menu_window.destroy()

    # Buttons im Hauptmenü-Fenster
    balance_button = tk.Button(main_menu_window, text="Kontostand", font=("Arial", 12), command=show_balance, bg=button_color, fg=text_color)
    balance_button.pack(pady=10)
    withdraw_button = tk.Button(main_menu_window, text="Abheben", font=("Arial", 12), command=withdraw, bg=button_color, fg=text_color)
    withdraw_button.pack(pady=10)
    deposit_button = tk.Button(main_menu_window, text="Einzahlen", font=("Arial", 12), command=deposit, bg=button_color, fg=text_color)
    deposit_button.pack(pady=10)
    transaction_button = tk.Button(main_menu_window, text="Letzte Transaktionen", font=("Arial", 12), command=show_transaction_history, bg=button_color, fg=text_color)
    transaction_button.pack(pady=10)
    change_pin_button = tk.Button(main_menu_window, text="PIN Ändern", font=("Arial", 12), command=show_change_pin_window, bg=button_color, fg=text_color)
    change_pin_button.pack(pady=10)
    quit_button = tk.Button(main_menu_window, text="Abbrechen", font=("Arial", 12), command=quit_program, bg=button_color, fg=text_color)
    quit_button.pack(pady=10)

    main_menu_window.mainloop()

# Funktion zum Überprüfen der PIN
def check_pin(pin_entry, pin_window):
    global counter
    global limit
    if pin_window and pin_window.winfo_exists():
        if pin_entry == pin:
            # Sicherheitsschlüssel generieren
            generate_security_key()
            # Schließe das PIN-Eingabefenster
            pin_window.destroy()
        else:
            counter += 1
            if counter >= limit:
                messagebox.showwarning("Warnung", "Karte gesperrt! Bitte kontaktieren Sie 0800 000 111")
            else:
                messagebox.showwarning("Warnung", f"Falscher PIN! Noch {limit - counter} Versuche übrig.")
                pin_entry.delete(0, tk.END)

# Funktion zum Generieren des Sicherheitsschlüssels
def generate_security_key():
    global security_key
    # Vierstellige Zufallszahl
    security_key = random.randint(1000, 9999)
    messagebox.showinfo("Sicherheitsschlüssel", f"Ihr Sicherheitsschlüssel lautet: {security_key}")
    verify_security_key()

# Funktion zur Überprüfung des Sicherheitsschlüssels
def verify_security_key():
    global security_key
    if security_key is not None:
        # Kurze Verzögerung zur Simulation
        time.sleep(5)  
        entered_key = simpledialog.askinteger("Sicherheitsschlüssel", "Bitte geben Sie den Sicherheitsschlüssel ein:")
        if entered_key == security_key:
            display_main_menu()
        else:
            messagebox.showerror("Fehler", "Falscher Sicherheitsschlüssel! Bitte versuchen Sie es erneut.")
            verify_security_key()

# Hauptfunktion des Programms
def main():
    # Erstellen des PIN-Eingabefensters
    pin_window = tk.Tk()
    pin_window.title("PIN Eingabe")
    # Hintergrundfarbe einstellen
    pin_window.configure(bg=background_color)  

    # Label und Eingabefeld für den PIN
    label = tk.Label(pin_window, text="Bitte geben Sie Ihren PIN ein:", font=("Arial", 12), bg=background_color, fg=text_color)
    label.pack(pady=10)
    pin_entry = tk.Entry(pin_window, font=("Arial", 12), show="*", width=20)
    pin_entry.pack(pady=10)

    # Button zum Bestätigen der PIN
    submit_button = tk.Button(pin_window, text="Bestätigen", font=("Arial", 12), command=lambda: check_pin(pin_entry.get(), pin_window), bg=button_color, fg=text_color)
    submit_button.pack(pady=10)

    pin_window.mainloop()

# Start des Programms
if __name__ == "__main__":
    main()
