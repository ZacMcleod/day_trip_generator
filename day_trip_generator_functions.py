import random
import time

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

def prompt_random_item_choice():
    choice = ''
    while choice != 'yes' and choice != 'no':
        choice = input(f'Would you like a random day trip for every variable?: (destinations, restaurants, transportations, entertainments): ').lower()
        if choice == 'yes':
            return True
            break
        elif choice == 'no':
            return False
            break
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
            break
        if choice in non_chosen_items:
            chosen_items.append(choice)
            non_chosen_items.remove(choice)
            item_count += 1
        elif choice == 'no' and item_count >= 1:
            return non_chosen_items
        else:
            print('Sorry, what?')
            continue



if prompt_random_item_choice():
    print(f'''Glad to hear it!
    Your Day Trip events include these in them:

    {random_destination}
    A {random_transportation}
    {random_entertainment}
    and a {random_restaurant}
    ''')
else:
    events_to_randomize = what_events_to_randomize(day_trip_lists_str)
    print(f'''Good to know!
Your Day Trip events include these in them:''')
    if 'destination' in events_to_randomize:
        print(random_destination)
    if 'transportation' in events_to_randomize:
        print(random_transportation)
    if 'entertainment' in events_to_randomize:
        print(random_entertainment)
    if 'restaurant' in events_to_randomize:
        print(random_restaurant)

    
