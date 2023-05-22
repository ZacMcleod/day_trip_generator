import random
import time


# Variables
destinations = ['The Grand Canyon', 'Washington DC', 'Seattle, Washington', 'New York City']
restaurants = ['Steak-House', 'Chinese restaurant', 'Mexican restaurant', 'Mongolian Barbecue', 'Food Truck']
transportations = ['Helicopter', 'Car', 'Plane', 'Train']
entertainments = ['Comedy Show', 'Amusement Park', 'Shopping Spree', 'Consert']

random_destination = random.choice(destinations)
random_restaurant = random.choice(restaurants)
random_transportation = random.choice(transportations)
random_entertainment = random.choice(entertainments)

day_trip_lists = [random_destination, random_restaurant, random_transportation, random_entertainment]
day_trip_lists_str = ['destination', 'restaurant', 'transportation', 'entertainment']


# Functions
def prompt_every_variable_choice():
    choice = ''
    while True:
        choice = input(f'Would you like a random day trip for every variable?: (destinations, restaurants, transportations, entertainments): ').lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print('''I'm sorry, I didn't get that...
                  ''')
            time.sleep(1)
            continue

def what_events_to_randomize(all_items):
    chosen_items = []
    non_chosen_items = []
    non_chosen_items = all_items.copy()
    print('''What events would you NOT like to randomize?: ''')
    item_count = 0
    while True:
        if item_count < 1:
            choice = input(f'''{non_chosen_items}?: ''').lower()
        elif item_count >= 1 and item_count < 3:
            choice = input(f'''Anything else?
            {non_chosen_items}?: ''').lower()
        else:
            return non_chosen_items
        if choice in non_chosen_items:
            chosen_items.append(choice)
            non_chosen_items.remove(choice)
            item_count += 1
        elif choice == 'no' and item_count >= 1:
            return non_chosen_items
        else:
            print('Sorry, what?')
            continue

def satisfied():
    satisfied = input("are you satisfied with the results? Type 'yes for completion or 'no' to regenerate Day Trip: ")
    if satisfied.lower() == 'yes':
        time.sleep(1)
        print('Complete')
        return True
    elif satisfied.lower() == 'no':
        time.sleep(1)
        print("Let's restart...")
        time.sleep(2)
        return False

def print_day_trip_events():
    print(f'''Good to know!
    Your Day Trip events include these in them:''')
    time.sleep(2)
    if 'destination' in events_to_randomize:
        print(random_destination)
        time.sleep(1)
    if 'transportation' in events_to_randomize:
        print(f'Riding {random_transportation}')
        time.sleep(1)
    if 'entertainment' in events_to_randomize:
        print(random_entertainment)
        time.sleep(1)
    if 'restaurant' in events_to_randomize:
        print(random_restaurant)
        time.sleep(1)

def welcome_to_day_trip_generator():
    print('''Welcome to Day Trip Generator!''')
    time.sleep(2)


# Day Trip Generator
welcome_to_day_trip_generator()
while True:
    if prompt_every_variable_choice():
        events_to_randomize = day_trip_lists_str
        print_day_trip_events()
        
    else:
        events_to_randomize = what_events_to_randomize(day_trip_lists_str)
        print_day_trip_events()

    if satisfied():
        break
    else:
        continue




