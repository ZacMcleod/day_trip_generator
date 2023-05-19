import random
from day_trip_generator import day_trip_lists

def random_list_item(day_trip_lists):
    random_choice = random.choice(list)
    return random_choice

def prompt_random_item_choice():
    choice = ''
    while choice != 'yes' and choice != 'no':
        choice = input(f'Would you like a random day trip for every variable?: destinations, restaurants, transportations, entertainments: ').lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print("I'm sorry, I didn't get that...")
            continue

def what_items_to_randomize(all_items):
    chosen_items = []
    print('''What events would you like to randomize?''')
    for item in all_items:
        choice_1 = input(f'{item}?').lower()
        if choice_1 == 'yes':
            chosen_items.append(item)