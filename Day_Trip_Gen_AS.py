import random


# (5 points): As a developer, I want to make at least three commits with descriptive messages. 
    # TBD
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists. 
destinations = ["Gulf Shores, AL", "Orange Beach, AL", "Destin, FL", "Jackson Hole, WY", "Elijay, GA" ]
restaurants = ["The Red Bar", "Original Oyster House", "Sea n Suds", "Outback Steakhouse", "McDonalds"]
modes_of_transportation = ["Car", "Train", "Bus", "Airplane", "Worm hole"]
entertainments = ["swimming", "jet-ski", "snow-ski", "hiking", "bicycle riding", "fishing", "dinner show", "site seeing"]

# (5 points): As a user, I want a destination to be randomly selected for my day trip. 

def pick_locations():
    
    dest_is_found = False
    while dest_is_found == False:
        chosen_dest = random.choice(destinations)
        print(f"Destination: {chosen_dest}")
        dest_input = input("Do you want to keep this selection? Yes or No:  ")
        if dest_input == "Yes":
            dest_is_found = True
            return chosen_dest
                      

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

def pick_eats():
    rest_is_found = False
    while rest_is_found == False:
        chosen_rest = random.choice(restaurants)
        print(f"Restaurant: {chosen_rest}")
        rest_input = input("Do you want to keep this selection? Yes or No:  ")
        if rest_input == "Yes":
            rest_is_found = True
            return chosen_rest



# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 

def pick_mode_trans():
    mode_is_found = False
    while mode_is_found == False:
        chosen_mode = random.choice(modes_of_transportation)
        print(f"Mode of Transportaion: {chosen_mode}")
        mode_input = input("Do you want to keep this selection? Yes or No:  ")
        if mode_input == "Yes":
            mode_is_found = True
            return chosen_mode

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 

def pick_entertainment():
    fun_is_found = False
    while fun_is_found == False:
        chosen_fun = random.choice(entertainments)
        print(f"Entertainment: {chosen_fun}")
        funt_input = input("Do you want to keep this selection? Yes or No:  ")
        if funt_input == "Yes":
            fun_is_found = True
            return chosen_fun

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 

def trip_itinerary():
    itinerary_is_found = False
    while itinerary_is_found == False:
        chosen_itinerary = (f"Your trip to {dest_result}, eating at {rest_result}, traveling by {transp_result}, while enjoying {entertain_result}")
        print(f"Itinerary: {chosen_itinerary}")
        itinery_input = input("Do you want to keep this selection? Yes or No:  ")
        if itinery_input == "Yes":
            itinerary_is_found = True
            return chosen_itinerary
        
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 

def trip_complete():
    trip_is_compl = False
    while trip_is_compl == False:
        compl_itinerary = (itinerary_result)
        print(f"{itinerary_result} is complete! Thank you for using Andy's Travel Service!")
        trip_compl_input = input(f"Do you wish to exit planner? Yes or No: ")
        if trip_compl_input == "Yes":
            trip_is_compl = True        

      
dest_result = pick_locations()
rest_result = pick_eats()
transp_result = pick_mode_trans()
entertain_result = pick_entertainment()
itinerary_result = trip_itinerary()
trip_complete()


# (10 points): As a user, I want to display my completed trip in the console. 

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!
