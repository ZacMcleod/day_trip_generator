from day_trip_generator_functions import prompt_random_item_choice, what_items_to_randomize, random

destinations = ['The Grand Canyon', 'Washington DC', 'Seattle, Washington', 'New York City']
restaurants = ['Steak-House', 'Chinese restaurant', 'Mexican restaurant', 'Mongolian Barbecue', 'Food Truck']
transportations = ['Helicopter', 'Car', 'Plane', 'Train']
entertainments = ['Comedy Show', 'Amusement Park', 'Shopping Spree', 'Consert']

day_trip_lists = [destinations, restaurants, transportations, entertainments]

random_destination = random.choice(destinations)
random_restaurant = random.choice(restaurants)
random_transportaion = random.choice(transportations)
random_entertainment = random.choice(entertainments)

if prompt_random_item_choice():
    print(f'''Glad to hear it!
    Your Day Trip events include these in them:

    {random_destination}
    A {random_transportaion}
    {random_entertainment}
    and a {random_restaurant}
    ''')
else:
    what_items_to_randomize(day_trip_lists)

