import sqlite3
import traceback


db = sqlite3.connect("chainsaw_db.db")

cursor = db.cursor()

def setup():

    cursor.execute('CREATE TABLE IF NOT EXISTS Record_Holders (Chainsaw_Juggling_Record_Holder text, Country text, Number_of_Catches Integer)' )

def add_record():

    name = input("Enter the name of the contestant: ")
    country = input("Enter the country of the contestant: ")
    catches = int(input("How many catches did they make: "))

    cursor.execute('INSERT INTO Record_Holders VALUES (? , ? , ?)', (name, country, catches))
    db.commit()


def delete_record():

    name = input("Enter the name of the contestant: ")

    cursor.execute('DELETE FROM Record_Holders WHERE Chainsaw_Juggling_Record_Holder = ?', (name,)) # Needed to make this a tuple, wierd.
    db.commit()

def update_record():

    name = input("Enter the name of the contestant: ")
    column = input("Do you want to update CATCHES or COUNTRY: ")


    if column == "catches":

        new_value = int(input("How may catches did they make: "))

        cursor.execute('UPDATE Record_Holders SET Number_of_Catches = ? WHERE Chainsaw_Juggling_Record_Holder = ?', (new_value, name))
        db.commit()

    elif column == "country":

        new_value = input("What country are they from: ")

        cursor.execute('UPDATE Record_Holders SET Country = ? WHERE Chainsaw_Juggling_Record_Holder = ?', (new_value, name))
        db.commit()

    else:

        print("not a valid entry")


def display_table():

    cursor.execute('SELECT * FROM Record_Holders' )

    for row in cursor:
        print(row)


def display_menu(): # Displays menu

    print('''

        1. Display table
        2. Add new record
        3. Delete record
        4. Update record
        q. Quit
    ''')

    choice = input("Please make a selection: ")

    return choice

def quit():

    db.close()



def handle_choice(choice): # Handles choices to clean up code.

    if choice == 1:

        display_table()

    elif choice == 2:

        add_record()

    elif choice == 3:

        delete_record()

    elif choice == 4:

        update_record()

    else:

        print("not a valid choice")


def main():

    setup()

    print("Welcome to the Chainsaw Juggling Program!")

    # Infite loop till User enters "q"
    while True:

        choice = display_menu()

        if choice == "q":

            quit()
            break

        elif choice.isdigit():
            handle_choice(int(choice))

        else:
            print("Not a valid choice")







main()
