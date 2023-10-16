import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Havaí': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianápolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jesey': 'Trenton',
    'New York': 'Albani',
    'Novo México': 'Santa Fé',
    'Oklahoma': 'Oklahoma City',
    'Ohio': 'Columbus',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Tennesse': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}
flag = 'continue'

state, capital = random.choice(list(capitals_dict.items())) #unpacking



while True:
    capital_answer = input(f"What is the capital of {state}: ").lower()

    if capital_answer == 'exit':
        print(f"The capital of '{state}' is '{capital}'.")
        print("Goodbye")
        break
    elif capitals_dict[state].lower() == capital_answer:
        print("Corect! Nice job")
        break


# capital = input(f"What is the capital of {key} state: ")

# for key_state, value_capital in capitals_dict.items():
#     if key_state == key:
#         if capital == value_capital:
#             print("Correct")
#         else:
#             capital = input(f"Try again: ")

    



