from random import randrange
from urllib.request import urlopen

def main():
    number = which_function()
    participants = import_participants("https://raw.githubusercontent.com/dejavu14868030/DrawMarch2020/master/participants.txt")
    to_run(number, participants)
    if_continue(number, participants)
    return_to_start(number, participants)

def which_function():
    number = 0
    while number != 1 and number != 2:
        try:
            number = input("Please enter 1 for draw simulation, or 2 to check if your name is in the list.")
            number = int(number)
        except:
            continue
    return number

def import_participants(url):
    list_of_participants = []
    for line in urlopen(url):
        list_of_participants.append(line.decode().strip())
    return list_of_participants

def to_run(num, list_of_participants):
    if num == 1:
        draw_simulation(list_of_participants)
    elif num == 2:
        check_list(list_of_participants)

def if_continue(num, list_of_participants):
    go_on = True
    print()
    while go_on:
        i = input("Do you want to continue? [Y/n]")
        if i == "" or i.lower() == "y":
            to_run(num, list_of_participants)
        elif i.lower() == "n":
            go_on = False

def return_to_start(num, list_of_participants):
    go_on = True
    print()
    while go_on:
        i = input("Do you want to return to main menu? [Y/n]")
        if i == "" or i.lower() == "y":
            main()
        elif i.lower() == "n":
            print()
            print("Thank you for using this service!")
            go_on = False

def draw_simulation(list_of_participants):
    i = 0
    print()
    print("Congratulations to the following winners:")
    while i < 10:
        print("@" + list_of_participants.pop(randrange(len(list_of_participants))))
        i += 1

def check_list(list_of_participants):
    to_check = str(input("Please enter the username you are looking for.   @"))
    count = 0
    print()
    for item in list_of_participants:
        if to_check.lower() in item.lower():
            print("@" + item)
            count += 1
    print()
    print("We have searched through the list and have found {} results.".format(count))
    print("If your name is not on the list, please contact me at your earliest convenience.")

main()
